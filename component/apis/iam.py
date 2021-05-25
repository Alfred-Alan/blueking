# -*- coding: utf-8 -*-
from ..base import ComponentAPI


class CollectionsIAM(object):
    """Collections of IAM APIS"""

    def __init__(self, client):
        self.client = client

        self.application = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/iam/application/',
            description=u'接入系统权限申请'
        )

        self.authorization_batch_instance = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/iam/authorization/batch_instance/',
            description=u'资源实例授权回收'
        )

        self.authorization_batch_path = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/iam/authorization/batch_path/',
            description=u'资源拓扑授权回收'
        )

        self.authorization_batch_resource_creator_action = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/iam/authorization/batch_resource_creator_action/',
            description=u'新建关联批量资源授权接口'
        )

        self.authorization_instance = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/iam/authorization/instance/',
            description=u'资源实例授权回收'
        )

        self.authorization_path = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/iam/authorization/path/',
            description=u'资源拓扑授权回收'
        )

        self.authorization_resource_creator_action = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/iam/authorization/resource_creator_action/',
            description=u'新建关联授权接口'
        )

        self.authorization_resource_creator_action_attribute = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/iam/authorization/resource_creator_action_attribute/',
            description=u'新建关联资源属性授权接口'
        )
