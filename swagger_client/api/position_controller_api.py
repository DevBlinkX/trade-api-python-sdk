# coding: utf-8

from __future__ import absolute_import

import re  # noqa: F401

import six

from swagger_client.api_client import ApiClient


class PositionControllerApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def convert_position(self, body, user_id, source, authorization, api_key):  # noqa: E501
        """Position Conversion  # noqa: E501

        :param api_key:
        :param authorization:
        :param PositionConversionRequest body: (required)
        :param str user_id: (required)
        :param str source: (required)
        :return: PositionConversionResponse.
        """
        (data) = self.convert_position_with_http_info(body, user_id, source, authorization, api_key)  # noqa: E501
        return data

    def convert_position_with_http_info(self, body, user_id, source, authorization, api_key):  # noqa: E501
        """Position Conversion  # noqa: E501

        :param api_key:
        :param authorization:
        :param PositionConversionRequest body: (required)
        :param str user_id: (required)
        :param str source: (required)
        :return: PositionConversionResponse.
        """

        all_params = ['body', 'user_id', 'source', 'authorization', 'api_key', 'async_req', '_return_http_data_only',
                      '_preload_content', '_request_timeout']  # noqa: E501

        params = locals()

        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `convert_position`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `convert_position`")  # noqa: E501
        # verify the required parameter 'source' is set
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `convert_position`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_quote`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_quote`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'user_id' in params:
            header_params['user-id'] = params['user_id']  # noqa: E501
        if 'source' in params:
            header_params['source'] = params['source']  # noqa: E501
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
            '/wrapper-order-service/api/portfolio/v1/convert-positions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PositionConversionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def do_holdings(self, user_id, source, authorization, api_key):  # noqa: E501
        """Holdings  # noqa: E501

        :param api_key:
        :param authorization:
        :param str user_id: (required)
        :param str source: (required)
        :return: HoldingResponse.
        """
        (data) = self.do_holdings_with_http_info(user_id, source, authorization, api_key)  # noqa: E501
        return data

    def do_holdings_with_http_info(self, user_id, source, authorization, api_key):  # noqa: E501
        """Holdings  # noqa: E501

        :param api_key:
        :param authorization:
        :param str user_id: (required)
        :param str source: (required)
        :return: HoldingResponse.
        """

        all_params = ['user_id', 'source', 'authorization', 'api_key', 'async_req', '_return_http_data_only',
                      '_preload_content', '_request_timeout']  # noqa: E501

        params = locals()

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `do_holdings`")  # noqa: E501
        # verify the required parameter 'source' is set
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `do_holdings`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_quote`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_quote`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'user_id' in params:
            header_params['user-id'] = params['user_id']  # noqa: E501
        if 'source' in params:
            header_params['source'] = params['source']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'api_key' in params:
            header_params['api-key'] = params['api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/wrapper-details-service/api/portfolio/v1/holdings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='HoldingResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_position_book(self, type, user_id, source, authorization, api_key):  # noqa: E501
        """Position Book  # noqa: E501

        :param type:
        :param api_key:
        :param authorization:
        :param str user_id: (required)
        :param str source: (required)
        :return: PositionBookResponse.
        """
        (data) = self.get_position_book_with_http_info(type, user_id, source, authorization, api_key)  # noqa: E501
        return data

    def get_position_book_with_http_info(self, type, user_id, source, authorization, api_key):  # noqa: E501
        """Position Book  # noqa: E501

        :param type:
        :param api_key:
        :param authorization:
        :param str user_id: (required)
        :param str source: (required)
        :return: PositionBookResponse.
        """

        all_params = ['type', 'user_id', 'source', 'authorization', 'api_key', 'async_req', '_return_http_data_only',
                      '_preload_content', '_request_timeout']  # noqa: E501

        params = locals()

        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_position_book`")  # noqa: E501
        # verify the required parameter 'source' is set
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `get_position_book`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `get_quote`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('api_key' not in params or
                params['api_key'] is None):
            raise ValueError("Missing the required parameter `api_key` when calling `get_quote`")  # noqa: E501
        # verify the required parameter 'api_key' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `get_quote`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

        header_params = {}
        if 'user_id' in params:
            header_params['user-id'] = params['user_id']  # noqa: E501
        if 'source' in params:
            header_params['source'] = params['source']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'api_key' in params:
            header_params['api-key'] = params['api_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/wrapper-details-service/api/portfolio/v1/position-book', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PositionBookResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
