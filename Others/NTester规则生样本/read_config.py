#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
"""
2017.01.17 每个文件都有读取配置信息的操作, 每次一换环境修改信息太麻烦, 还是专门用一个读取配置文件的类来搞定吧
"""
import configparser

__author__ = '__L1n__w@tch'


class ConfigReader:
    def __init__(self):
        self.cp = configparser.ConfigParser()

    def read_section_fields(self, file_path, section, fields):
        """
        读取指定文件中, 指定节的指定字段
        :param file_path: str(), 配置文件路径
        :param section: str(), 指定节
        :param fields: list(), 指定字段
        :return: list(), 每一个字段的值
        """

        self.cp.read(file_path)

        result_list = list()

        for each_field in fields:
            result_list.append(self.cp.get(section, each_field))

        return result_list

    def read_af_back_info(self, file_path):
        """
        读取 af 后台文件的相关信息
        :param file_path: str(), 配置文件路径
        :return:
        """
        section_name = "af"
        fields = ["af_ip", "af_port", "af_back_user", "af_back_password"]
        return self.read_section_fields(file_path, section_name, fields)

    def read_mysql_info(self, file_path):
        """
        读取 af 后台 mysql 相关信息
        :param file_path: str(), 配置文件路径
        :return:
        """
        section_name = "mysql"
        fields = ["db_host", "db_user", "db_password", "db_name"]
        return self.read_section_fields(file_path, section_name, fields)

    def read_ip_info(self, file_path):
        """
        读取本地 IP 及测试 IP
        :param file_path: str(), 配置文件路径
        :return:
        """
        section_name = "test_ip"
        fields = ["local_ip_address", "target_ip_address"]
        return self.read_section_fields(file_path, section_name, fields)

    def read_des_info(self, file_path):
        """
        读取 DES 相关信息
        :param file_path: str(), 配置文件路径
        :return:
        """
        section_name = "Others"
        fields = ["des_key", "des_iv"]
        return self.read_section_fields(file_path, section_name, fields)

    def read_lib_info(self, file_path):
        """
        读取最终 sqlite 库信息
        :param file_path: str(), 配置文件路径
        :return:
        """
        section_name = "Others"
        fields = ["result_lib_name", "result_waf_ips_table_name", "result_utm_table_name"]
        return self.read_section_fields(file_path, section_name, fields)


if __name__ == "__main__":
    pass
