from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class Trs(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, variables=None, rules=None, interpretations=None):  # noqa: E501
        """Trs - a model defined in OpenAPI

        :param variables: The variables of this Trs.  # noqa: E501
        :type variables: List[str]
        :param rules: The rules of this Trs.  # noqa: E501
        :type rules: List[str]
        :param interpretations: The interpretations of this Trs.  # noqa: E501
        :type interpretations: List[str]
        """
        self.openapi_types = {
            'variables': List[str],
            'rules': List[str],
            'interpretations': List[str]
        }

        self.attribute_map = {
            'variables': 'variables',
            'rules': 'rules',
            'interpretations': 'interpretations'
        }

        self._variables = variables
        self._rules = rules
        self._interpretations = interpretations

    @classmethod
    def from_dict(cls, dikt) -> 'Trs':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Trs of this Trs.  # noqa: E501
        :rtype: Trs
        """
        return util.deserialize_model(dikt, cls)

    @property
    def variables(self) -> List[str]:
        """Gets the variables of this Trs.


        :return: The variables of this Trs.
        :rtype: List[str]
        """
        return self._variables

    @variables.setter
    def variables(self, variables: List[str]):
        """Sets the variables of this Trs.


        :param variables: The variables of this Trs.
        :type variables: List[str]
        """
        if variables is None:
            raise ValueError("Invalid value for `variables`, must not be `None`")  # noqa: E501
        if variables is not None and len(variables) < 1:
            raise ValueError("Invalid value for `variables`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._variables = variables

    @property
    def rules(self) -> List[str]:
        """Gets the rules of this Trs.


        :return: The rules of this Trs.
        :rtype: List[str]
        """
        return self._rules

    @rules.setter
    def rules(self, rules: List[str]):
        """Sets the rules of this Trs.


        :param rules: The rules of this Trs.
        :type rules: List[str]
        """
        if rules is None:
            raise ValueError("Invalid value for `rules`, must not be `None`")  # noqa: E501
        if rules is not None and len(rules) < 1:
            raise ValueError("Invalid value for `rules`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._rules = rules

    @property
    def interpretations(self) -> List[str]:
        """Gets the interpretations of this Trs.


        :return: The interpretations of this Trs.
        :rtype: List[str]
        """
        return self._interpretations

    @interpretations.setter
    def interpretations(self, interpretations: List[str]):
        """Sets the interpretations of this Trs.


        :param interpretations: The interpretations of this Trs.
        :type interpretations: List[str]
        """
        if interpretations is None:
            raise ValueError("Invalid value for `interpretations`, must not be `None`")  # noqa: E501
        if interpretations is not None and len(interpretations) < 1:
            raise ValueError("Invalid value for `interpretations`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._interpretations = interpretations
