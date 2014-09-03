
from django_utils.request import is_ip_in_range, is_ip_in_list
from unittest import TestCase


class Request(TestCase):
    test_ranges = [
        ('2.9.1.50', '2.11.255.40'),
        ('3.90.1.87', '5.30.2.87'),
        ' 127.0.0.1'
    ]
    success_test_ips = [
        ['2.9.1.50', '2.9.1.51', '2.11.255.40', '2.11.255.39', '2.10.10.10', '2.9.2.45'],
        ['3.90.1.87', '5.30.2.87', '5.30.2.86', '3.90.1.88', '4.90.1.88', '4.60.3.88'],
        ['127.0.0.1']
    ]
    fail_test_ips = [
        '2.60.3.88', '6.60.3.88', '5.30.2.88', '3.90.1.86',
        '2.9.1.49', '2.11.255.41', '2.13.55.45'
    ]

    def test_is_ip_in_range(self):
        test_row = 0
        start = self.test_ranges[test_row][0]
        end = self.test_ranges[test_row][1]
        for ip in self.success_test_ips[test_row]:
            self.assertEqual(is_ip_in_range(ip, start, end), True)
        for ip in self.fail_test_ips:
            self.assertEqual(is_ip_in_range(ip, start, end), False)

    def test_is_ip_in_list(self):
        for group in self.success_test_ips:
            for ip in group:
                self.assertEqual(is_ip_in_list(ip, self.test_ranges), True)
        for ip in self.fail_test_ips:
            self.assertEqual(is_ip_in_list(ip, self.test_ranges), False)
