# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class NumberList(ListResource):
    """  """

    def __init__(self, version):
        """
        Initialize the NumberList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.pricing.v1.voice.number.NumberList
        :rtype: twilio.rest.pricing.v1.voice.number.NumberList
        """
        super(NumberList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self, number):
        """
        Constructs a NumberContext

        :param number: The number

        :returns: twilio.rest.pricing.v1.voice.number.NumberContext
        :rtype: twilio.rest.pricing.v1.voice.number.NumberContext
        """
        return NumberContext(self._version, number=number, )

    def __call__(self, number):
        """
        Constructs a NumberContext

        :param number: The number

        :returns: twilio.rest.pricing.v1.voice.number.NumberContext
        :rtype: twilio.rest.pricing.v1.voice.number.NumberContext
        """
        return NumberContext(self._version, number=number, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Pricing.V1.NumberList>'


class NumberPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the NumberPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.pricing.v1.voice.number.NumberPage
        :rtype: twilio.rest.pricing.v1.voice.number.NumberPage
        """
        super(NumberPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of NumberInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.pricing.v1.voice.number.NumberInstance
        :rtype: twilio.rest.pricing.v1.voice.number.NumberInstance
        """
        return NumberInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Pricing.V1.NumberPage>'


class NumberContext(InstanceContext):
    """  """

    def __init__(self, version, number):
        """
        Initialize the NumberContext

        :param Version version: Version that contains the resource
        :param number: The number

        :returns: twilio.rest.pricing.v1.voice.number.NumberContext
        :rtype: twilio.rest.pricing.v1.voice.number.NumberContext
        """
        super(NumberContext, self).__init__(version)

        # Path Solution
        self._solution = {'number': number, }
        self._uri = '/Voice/Numbers/{number}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a NumberInstance

        :returns: Fetched NumberInstance
        :rtype: twilio.rest.pricing.v1.voice.number.NumberInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return NumberInstance(self._version, payload, number=self._solution['number'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Pricing.V1.NumberContext {}>'.format(context)


class NumberInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, number=None):
        """
        Initialize the NumberInstance

        :returns: twilio.rest.pricing.v1.voice.number.NumberInstance
        :rtype: twilio.rest.pricing.v1.voice.number.NumberInstance
        """
        super(NumberInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'number': payload['number'],
            'country': payload['country'],
            'iso_country': payload['iso_country'],
            'outbound_call_price': payload['outbound_call_price'],
            'inbound_call_price': payload['inbound_call_price'],
            'price_unit': payload['price_unit'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'number': number or self._properties['number'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: NumberContext for this NumberInstance
        :rtype: twilio.rest.pricing.v1.voice.number.NumberContext
        """
        if self._context is None:
            self._context = NumberContext(self._version, number=self._solution['number'], )
        return self._context

    @property
    def number(self):
        """
        :returns: The number
        :rtype: unicode
        """
        return self._properties['number']

    @property
    def country(self):
        """
        :returns: Name of the country
        :rtype: unicode
        """
        return self._properties['country']

    @property
    def iso_country(self):
        """
        :returns: The ISO country code
        :rtype: unicode
        """
        return self._properties['iso_country']

    @property
    def outbound_call_price(self):
        """
        :returns: See OutboundCallPrice record
        :rtype: unicode
        """
        return self._properties['outbound_call_price']

    @property
    def inbound_call_price(self):
        """
        :returns: See InboundCallPrice record (returned as null if the Phone Number provided is not a Twilio number owned by this account)
        :rtype: unicode
        """
        return self._properties['inbound_call_price']

    @property
    def price_unit(self):
        """
        :returns: The currency in which prices are measured, in ISO 4127 format (e.g. usd, eur, jpy).
        :rtype: unicode
        """
        return self._properties['price_unit']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a NumberInstance

        :returns: Fetched NumberInstance
        :rtype: twilio.rest.pricing.v1.voice.number.NumberInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Pricing.V1.NumberInstance {}>'.format(context)
