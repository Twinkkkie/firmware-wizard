import unittest

from firmware_wizard.core import build_dry_run_command, load_manifest


class FirmwareWizardDemoTests(unittest.TestCase):
    def test_manifest_and_dry_run_command(self):
        package = load_manifest("examples/manifest.json")[0]
        command = build_dry_run_command(package, "COM7")
        self.assertEqual(command[0], "sam-ba")
        self.assertIn("COM7", command)
        self.assertIn("--firmware", command)

    def test_integrity_failure(self):
        package = load_manifest("examples/manifest.json")[0]
        bad = type(package)(package.device, package.version, package.file, "0" * 64)
        with self.assertRaises(ValueError):
            build_dry_run_command(bad, "COM1")


if __name__ == "__main__":
    unittest.main()
