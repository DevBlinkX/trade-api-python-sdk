# coding: utf-8

from __future__ import absolute_import

import re  # noqa: F401

from swagger_client.api_client import ApiClient


class TradeDetailsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def order_details(self, body, authorization, api_key):  # noqa: E501
        """OrderDetailsAPI  # noqa: E501

        :param TradeDetailsRequest body: (required)
        :param str authorization: (required)
        :param str api_key: (required)
        :return: TradeDetailsSuccess.
        """
        (data) = self.order_details_with_http_info(body, authorization, api_key)  # noqa: E501
        return data

    def order_details_with_http_info(self, body, authorization, api_key):  # noqa: E501
        """OrderDetailsAPI  # noqa: E501

        :param TradeDetailsRequest body: (required)
        :param str authorization: (required)
        :param str api_key: (required)
        :return: TradeDetailsSuccess.
        """

        all_params = ['body', 'authorization', 'api_key', 'async_req', '_return_http_data_only', '_preload_content',
                      '_request_timeout']  # noqa: E501

        params = locals()

        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `order_details`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError(
                "Missing the required parameter `authorization` when calling `order_details`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `order_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'api_key' in params:
            header_params['api-key'] = params['api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/wrapper-details-service/api/order/v1/order-details', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TradeDetailsSuccess',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def order_history(self, authorization, api_key):  # noqa: E501
        """Order History API  # noqa: E501

        :param str authorization: (required)
        :param str api_key: (required)
        :return: OrderHistorySuccess.
        """
        (data) = self.order_history_with_http_info(authorization, api_key)  # noqa: E501
        return data

    def order_history_with_http_info(self, authorization, api_key):  # noqa: E501
        """Order History API  # noqa: E501

        :param str authorization: (required)
        :param str api_key: (required)
        :return: OrderHistorySuccess.
        """

        all_params = ['authorization', 'api_key', 'body', 'async_req', '_return_http_data_only', '_preload_content',
                      '_request_timeout']  # noqa: E501

        params = locals()

        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError(
                "Missing the required parameter `authorization` when calling `order_history`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `order_history`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'api_key' in params:
            header_params['api-key'] = params['api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/wrapper-details-service/api/order/v1/order-history', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderHistorySuccess',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def trade_details_using_order_id(self, body, authorization, api_key):  # noqa: E501
        """TradeDetails Using OrderId API  # noqa: E501

        :param TradeDetailsRequest body: (required)
        :param str authorization: (required)
        :param str api_key: (required)
        :return: TradeDetailsSuccess
                 If the method is called asynchronously,
                 returns the request thread.
        """
        (data) = self.trade_details_using_order_id_with_http_info(body, authorization, api_key)  # noqa: E501
        return data

    def trade_details_using_order_id_with_http_info(self, body, authorization, api_key):  # noqa: E501
        """TradeDetails Using OrderId API  # noqa: E501

        :param TradeDetailsRequest body: (required)
        :param str authorization: (required)
        :param str api_key: (required)
        :return: TradeDetailsSuccess.
        """

        all_params = ['body', 'authorization', 'api_key', 'async_req', '_return_http_data_only', '_preload_content',
                      '_request_timeout']  # noqa: E501

        params = locals()

        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError(
                "Missing the required parameter `body` when calling `trade_details_using_order_id`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError(
                "Missing the required parameter `authorization` when calling `trade_details_using_order_id`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError(
                "Missing the required parameter `api_key` when calling `trade_details_using_order_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'api_key' in params:
            header_params['api-key'] = params['api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/wrapper-details-service/api/order/v1/trade-details', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TradeDetailsSuccess',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
