import unittest
import src.traceroute_class as test_class


class MyTestCase(unittest.TestCase):

    def test_init(self):
        test_object = test_class.HandleTraceroute
        if not test_object:
            assert False
        else:
            with self.subTest('Testing object is correct class type'):
                self.assertIsInstance(test_object, test_class.HandleTraceroute)
            with self.subTest('Testing contents of class'):
                self.assertEqual(test_object.a_pipper, '169')
            # can check more instance creation types


    def test_check_ip_address_if_external(self):
        test_object = test_class.HandleTraceroute
        if not test_object:
            assert False
        else:
            with self.subTest('Testing straight after initialisation that nothing is in EXT_IP_ADDRESS'):
                self.assertTrue(test_object.is_external_address_empty())
            with self.subTest('Testing the validity of an address.'):
                test_object.__init__().hops = ['192.168.0.1', '192.168.0.2','99.99.99.1', '8.8.8.8']
                self.assertTrue(test_object.check_ip_address_if_external('99.99.08.7'))

    def test_do_traceroute(self):
        """
        Testing that a traceroute has been successful.
        :return:
        """
        test_object = test_class.HandleTraceroute
        test_object.show_details()
        if not test_object:
            assert False
        else:
            with self.subTest('Testing default target'):
                test_object.do_traceroute()
                self.assertFalse(test_object.is_external_address_empty())
            with self.subTest('Testing a valid non-default target address.'):
                test_object.do_traceroute('1.1.1.1')
            with self.subTest('Testing a non-valid target address.'):
                test_object.do_traceroute('192.168.1.1')



    def test_print_hops(self):
        assert False

    def test_get_hops(self):
        assert False

    def test_test_loop_return(self):
        assert False

    def test_set_external_ip_address(self):
        assert False

    def test_set_external_ip_address_to_env_var(self):
        assert False

    def test_show_details(self):
        assert False

    def test_get_existing_external_ip_address(self):
        assert False

    def test_get_external_ip_address(self):
        assert False



if __name__ == '__main__':
    unittest.main()
