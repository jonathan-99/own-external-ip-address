try:
    from icmplib import traceroute
    import sys
    import json
    import os
except ImportError as e:
    sys.exit("Importing error: " + str(e))

class HostMachineChecker:

    def __init__(self):
        self.host_machine_env_var = ""
        self.host_machine_env_var_name = 'EXT_IP_ADDRESS'
        self.host_os = ""
        self.linux_path = "~/opt/mnt/"
        self.windows_path = "C:/Users/JonathanL/"

    def set_class_variables(self, name, value) -> bool:
        try:
            temp_name = 'self' + str(name)
            temp_name = str(value)
            return True
        except Exception as err:
            print('An error in set_class_variable: {}'.format(str(err)))
            return False


    def check_host_os(self) -> str:
        """
        If host machine is of linux type, return "linux" else "windows
        :param self:
        :return:
        """
        pass

    def get_existing_external_ip_address(self) -> str:
        return os.environ[self.host_machine_env_var_name]

    def set_host_machine_env_var(self) -> bool:
        try:
            os.environ.putenv(self.host_machine_env_var_name, self.host_machine_env_var)
            return True
        except Exception as e:
            sys.exit('Error in set-host_machine_env_var: {}'.format(str(e)))
            return False

