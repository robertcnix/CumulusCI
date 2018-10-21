import unittest

from cumulusci.core.config import MergedConfig, MergedYamlConfig
from cumulusci.core.exceptions import ConfigMergeError


class TestMergedConfig(unittest.TestCase):
    def test_init(self):
        config = MergedConfig(
            user_config={"hello": "christian"}, global_config={"hello": "world"}
        )
        self.assertEqual(config.hello, "christian")

    def test_merge_failure(self):
        with self.assertRaises(ConfigMergeError) as cm:
            config = MergedConfig(
                user_config={"hello": "christian", "test": [1, 2]},
                global_config={"hello": "world", "test": {"sample": 1}},
            )
        exception = cm.exception
        self.assertEqual(exception.config_name, "user_config")

    def test_merged_yaml_init(self):
        config = MergedYamlConfig(
            user_config='{"hello": "christian"}', global_config='{"hello": "world"}'
        )

        self.assertEqual(config.hello, "christian")