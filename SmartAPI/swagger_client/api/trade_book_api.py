# coding: utf-8

"""
    portfolio-services Api Doc

    Rest APIs  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: sales@marketsimplified.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class TradeBookApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_order_book(self, user_id, source, **kwargs):  # noqa: E501
        """Get orders  # noqa: E501

        This endpoint allows users view orders  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_order_book(user_id, source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :param str source: (required)
        :return: OrderBookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_order_book_with_http_info(user_id, source, **kwargs)  # noqa: E501
        else:
            (data) = self.get_order_book_with_http_info(user_id, source, **kwargs)  # noqa: E501
            return data

    def get_order_book_with_http_info(self, user_id, source, **kwargs):  # noqa: E501
        """Get orders  # noqa: E501

        This endpoint allows users view orders  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_order_book_with_http_info(user_id, source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :param str source: (required)
        :return: OrderBookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'source']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_book" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_order_book`")  # noqa: E501
        # verify the required parameter 'source' is set
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `get_order_book`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'user_id' in params:
            header_params['user-id'] = params['user_id']  # noqa: E501
        if 'source' in params:
            header_params['source'] = params['source']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/order/v1/order-book', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderBookResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_order_trail(self, body, user_id, source, **kwargs):  # noqa: E501
        """Order Trail  # noqa: E501

        This endpoint allows users to get events of particular order  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_order_trail(body, user_id, source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OrderTrailRequest body: (required)
        :param str user_id: (required)
        :param str source: (required)
        :return: OrderTrailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_order_trail_with_http_info(body, user_id, source, **kwargs)  # noqa: E501
        else:
            (data) = self.get_order_trail_with_http_info(body, user_id, source, **kwargs)  # noqa: E501
            return data

    def get_order_trail_with_http_info(self, body, user_id, source, **kwargs):  # noqa: E501
        """Order Trail  # noqa: E501

        This endpoint allows users to get events of particular order  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_order_trail_with_http_info(body, user_id, source, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param OrderTrailRequest body: (required)
        :param str user_id: (required)
        :param str source: (required)
        :return: OrderTrailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'user_id', 'source']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_trail" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `get_order_trail`")  # noqa: E501
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `get_order_trail`")  # noqa: E501
        # verify the required parameter 'source' is set
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `get_order_trail`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'user_id' in params:
            header_params['user-id'] = params['user_id']  # noqa: E501
        if 'source' in params:
            header_params['source'] = params['source']  # noqa: E501

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
            '/order/v1/order-trail', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderTrailResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def trade_book(self, user_id, source, order_ids, **kwargs):  # noqa: E501
        """Trades  # noqa: E501

        This endpoint allows users to view trades  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trade_book(user_id, source, order_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :param str source: (required)
        :param list[str] order_ids: (required)
        :return: TradeBookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.trade_book_with_http_info(user_id, source, order_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.trade_book_with_http_info(user_id, source, order_ids, **kwargs)  # noqa: E501
            return data

    def trade_book_with_http_info(self, user_id, source, order_ids, **kwargs):  # noqa: E501
        """Trades  # noqa: E501

        This endpoint allows users to view trades  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.trade_book_with_http_info(user_id, source, order_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str user_id: (required)
        :param str source: (required)
        :param list[str] order_ids: (required)
        :return: TradeBookResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'source', 'order_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trade_book" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `trade_book`")  # noqa: E501
        # verify the required parameter 'source' is set
        if ('source' not in params or
                params['source'] is None):
            raise ValueError("Missing the required parameter `source` when calling `trade_book`")  # noqa: E501
        # verify the required parameter 'order_ids' is set
        if ('order_ids' not in params or
                params['order_ids'] is None):
            raise ValueError("Missing the required parameter `order_ids` when calling `trade_book`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_ids' in params:
            query_params.append(('orderIds', params['order_ids']))  # noqa: E501
            collection_formats['orderIds'] = 'multi'  # noqa: E501

        header_params = {}
        if 'user_id' in params:
            header_params['user-id'] = params['user_id']  # noqa: E501
        if 'source' in params:
            header_params['source'] = params['source']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/order/v1/trade-book', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TradeBookResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)