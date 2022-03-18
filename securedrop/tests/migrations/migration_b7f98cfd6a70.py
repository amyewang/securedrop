import uuid

from sqlalchemy import text

from db import db
from journalist_app import create_app


# Random, chosen by fair dice roll
FILESYSTEM_ID = 'FPLIUY3FWFROQ52YHDMXFYKOTIK2FT4GAFN6HTCPPG3TSNAHYOPDDT5C3TR' \
                'JWDV2IL3JDOS4NFAJNEI73KRQ7HQEVNAF35UCCW5M7VI='


class UpgradeTester:
    """Insert a source, verify the filesystem_id makes it through untouched
    """

    def __init__(self, config):
        """This function MUST accept an argument named `config`.
           You will likely want to save a reference to the config in your
           class, so you can access the database later.
        """
        self.config = config
        self.app = create_app(config)

    def load_data(self):
        """This function loads data into the database and filesystem. It is
           executed before the upgrade.
        """
        with self.app.app_context():
            params = {
                'uuid': str(uuid.uuid4()),
                'filesystem_id': FILESYSTEM_ID,
                'journalist_designation': 'sunburned arraignment',
                'interaction_count': 0,
            }
            sql = """\
                INSERT INTO sources (uuid, filesystem_id, journalist_designation, interaction_count)
                VALUES (:uuid, :filesystem_id, :journalist_designation, :interaction_count);"""
            db.engine.execute(text(sql), **params)

    def check_upgrade(self):
        """This function is run after the upgrade and verifies the state
           of the database or filesystem. It MUST raise an exception if the
           check fails.
        """
        with self.app.app_context():
            source = db.engine.execute(
                'SELECT filesystem_id FROM sources'
            ).first()
            assert source[0] == FILESYSTEM_ID


class DowngradeTester:
    """Downgrading only makes fields nullable again, which is a
    non-destructive and safe operation"""

    def __init__(self, config):
        """This function MUST accept an argument named `config`.
           You will likely want to save a reference to the config in your
           class, so you can access the database later.
        """
        self.config = config

    def load_data(self):
        """This function loads data into the database and filesystem. It is
           executed before the downgrade.
        """
        pass

    def check_downgrade(self):
        """This function is run after the downgrade and verifies the state
           of the database or filesystem. It MUST raise an exception if the
           check fails.
        """
        pass
