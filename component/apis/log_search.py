# -*- coding: utf-8 -*-
from ..base import ComponentAPI


class CollectionsLogSearch(object):
    """Collections of LogSearch APIS"""

    def __init__(self, client):
        self.client = client

        self.esquery_search = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/log_search/esquery_search/',
            description=u'日志查询接口'
        )