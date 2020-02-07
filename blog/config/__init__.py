from .dev import DevConfig
from .dev import TestConfig
from .dev import ProductionConfig

app_config = {'dev': DevConfig,
              'test': TestConfig,
              'production': ProductionConfig}
