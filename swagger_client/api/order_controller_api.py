# coding: utf-8

from __future__ import absolute_import

import re  # noqa: F401

from swagger_client.api_client import ApiClient


class OrderControllerApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def brokerage_charges(self, body, user_id, authorization, api_key, source):  # noqa: E501
        """Brokerage Charges  # noqa: E501

        :param api_key:
        :param authorization:
        :param BrokerageChargeRequest body: (required)
        :param str user_id: (required)
        :param str source: (required)
        :return: BrokerageChargeResponse.
        """
        (data) = self.brokerage_charges_with_http_info(body, user_id, authorization, api_key, source)  # noqa: E501
        return data

    def brokerage_charges_with_http_info(self, body, user_id, authorization, api_key, source):  # noqa: E501
        """Brokerage Charges  # noqa: E501

        :param api_key:
        :param authorization:
        :param BrokerageChargeRequest body: (required)
        :param str user_id: (required)
        :param str source: (required)
        :return: BrokerageChargeResponse.
        """

        all_params = ['body', 'user_id', 'authorization', 'api_key', 'source', 'async_req', '_return_http_data_only',
                      '_preload_content',
                      '_request_timeout']  # noqa: E501

        params = locals()

        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `brokerage_charges`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `brokerage_charges`")  # noqa: E501
        # verify the required parameter 'source' is set
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `brokerage_charges`")  # noqa: E501
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
            '/wrapper-details-service/api/trade/v1/brokerage', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BrokerageChargeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def cancel_order(self, body, user_id, source, authorization, api_key):  # noqa: E501
        """Cancel Order  # noqa: E501

        :param api_key:
        :param authorization:
        :param CancelOrderRequest body: (required)
        :param str user_id: (required)
        :param str source: (required)
        :return: CancelOrderResponse.
        """
        (data) = self.cancel_order_with_http_info(body, user_id, source, authorization, api_key)  # noqa: E501
        return data

    def cancel_order_with_http_info(self, body, user_id, source, authorization, api_key):
        # noqa: E501
        """Cancel Order  # noqa: E501

        :param api_key:
        :param authorization:
        :param CancelOrderRequest body: (required)
        :param str user_id: (required)
        :param str source: (required)
        :return: CancelOrderResponse.
        """

        all_params = ['body', 'user_id', 'source', 'authorization', 'api_key', 'async_req', '_return_http_data_only',
                      '_preload_content',
                      '_request_timeout']  # noqa: E501

        params = locals()

        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `cancel_order`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `cancel_order`")  # noqa: E501
        # verify the required parameter 'source' is set
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `cancel_order`")  # noqa: E501
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
            '/wrapper-order-service/api/order/v1/cancel-order', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CancelOrderResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def exit_order(self, body, user_id, source, authorization, api_key):  # noqa: E501
        """Exit an Order  # noqa: E501

        :param api_key:
        :param authorization:
        :param ExitOrderRequest body: (required)
        :param str user_id: (required)
        :param str source: (required)
        :return: ExitOrderResponse.
        """
        (data) = self.exit_order_with_http_info(body, user_id, source, authorization, api_key)  # noqa: E501
        return data

    def exit_order_with_http_info(self, body, user_id, source, authorization, api_key):  # noqa: E501
        """Exit an Order  # noqa: E501

        :param api_key:
        :param authorization:
        :param ExitOrderRequest body: (required)
        :param str user_id: (required)
        :param str source: (required)
        :return: ExitOrderResponse.
        """

        all_params = ['body', 'user_id', 'source', 'authorization', 'api_key', 'async_req', '_return_http_data_only',
                      '_preload_content', '_request_timeout']  # noqa: E501

        params = locals()

        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `exit_order`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `exit_order`")  # noqa: E501
        # verify the required parameter 'source' is set
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `exit_order`")  # noqa: E501
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
            '/order/v1/exit-order', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExitOrderResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_order(self, body, user_id, source, authorization, api_key):  # noqa: E501
        """Modify Order  # noqa: E501

        :param api_key:
        :param authorization:
        :param ModifyOrderRequest body: (required)
        :param str user_id: (required)
        :param str source: (required)
        :return: ModifyOrderResponse.
        """
        (data) = self.modify_order_with_http_info(body, user_id, source, authorization, api_key)  # noqa: E501
        return data

    def modify_order_with_http_info(self, body, user_id, source, authorization, api_key):  # noqa: E501
        """Modify Order  # noqa: E501

        :param api_key:
        :param authorization:
        :param ModifyOrderRequest body: (required)
        :param str user_id: (required)
        :param str source: (required)
        :return: ModifyOrderResponse.
        """

        all_params = ['body', 'user_id', 'source', 'authorization', 'api_key', 'async_req', '_return_http_data_only',
                      '_preload_content', '_request_timeout']  # noqa: E501

        params = locals()

        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `modify_order`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `modify_order`")  # noqa: E501
        # verify the required parameter 'source' is set
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `modify_order`")  # noqa: E501
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
            '/wrapper-order-service/api/order/v1/modify-order', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModifyOrderResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def place_order(self, body, user_id, source, authorization, api_key):  # noqa: E501
        """Place Order  # noqa: E501

        :param api_key:
        :param authorization:
        :param PlaceOrderRequest body: (required)
        :param str user_id: (required)
        :param str source: (required)
        :return: PlaceOrderResponse.
        """
        (data) = self.place_order_with_http_info(body, user_id, source, authorization, api_key)  # noqa: E501
        return data

    def place_order_with_http_info(self, body, user_id, source, authorization, api_key):  # noqa: E501
        """Place Order  # noqa: E501

        :param api_key:
        :param authorization:
        :param PlaceOrderRequest body: (required)
        :param str user_id: (required)
        :param str source: (required)
        :return: PlaceOrderResponse.
        """

        all_params = ['body', 'user_id', 'source', 'authorization', 'api_key', 'async_req', '_return_http_data_only',
                      '_preload_content', '_request_timeout']  # noqa: E501

        params = locals()

        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `place_order`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `place_order`")  # noqa: E501
        # verify the required parameter 'source' is set
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `place_order`")  # noqa: E501
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
            '/wrapper-order-service/api/order/v1/place-order', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PlaceOrderResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
