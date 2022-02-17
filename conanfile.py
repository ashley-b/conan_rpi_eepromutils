from conans import ConanFile, AutoToolsBuildEnvironment, tools

required_conan_version = ">=1.43.0"

class RpiEepromutilsConan(ConanFile):
    name = "rpi_eepromutils"
    license = "BSD-3-Clause"
    homepage = "https://github.com/raspberrypi/hats"
    url = "github.com/ashley-b/conan_rpi_eepromutils"
    description = "Utilities to create, flash and dump HAT EEPROM images"
    topics = ("EEPROM", "RPi")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    @property
    def _source_dir(self):
        return "hats/eepromutils/"

    @property
    def _make_args(self):
        return [ "prefix={}".format(self.package_folder) ]

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        tools.get(**self.conan_data["sources"][self.version],
                  destination="hats", strip_root=True)

    def build(self):
        with tools.chdir(self._source_dir):
            autotools = AutoToolsBuildEnvironment(self)
            autotools.make(args=self._make_args)

    def package(self):
        self.copy("LICENCE", src="hats")
#        autotools = AutoToolsBuildEnvironment(self)
#        with tools.chdir(self._source_dir):
#            autotools.install(args=self._make_args)
        self.copy("eepmake", src=self._source_dir, dst="bin")
        self.copy("eepdump", src=self._source_dir, dst="bin")
        self.copy("eepflash.sh", src=self._source_dir, dst="bin")
