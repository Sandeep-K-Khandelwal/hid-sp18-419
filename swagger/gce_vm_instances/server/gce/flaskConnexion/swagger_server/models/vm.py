# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.definition_disk import DefinitionDISK  # noqa: F401,E501
from swagger_server.models.vm_tags import VMTags  # noqa: F401,E501
from swagger_server import util


class VM(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id=None, creation_timestamp=None, name=None, description=None, tags=None, machine_type=None, status=None, can_ip_forward=None, cpu_platform=None, deletion_protection=None, disks=None, kind=None, label_fingerprint=None):  # noqa: E501
        """VM - a model defined in Swagger

        :param id: The id of this VM.  # noqa: E501
        :type id: str
        :param creation_timestamp: The creation_timestamp of this VM.  # noqa: E501
        :type creation_timestamp: datetime
        :param name: The name of this VM.  # noqa: E501
        :type name: str
        :param description: The description of this VM.  # noqa: E501
        :type description: str
        :param tags: The tags of this VM.  # noqa: E501
        :type tags: VMTags
        :param machine_type: The machine_type of this VM.  # noqa: E501
        :type machine_type: str
        :param status: The status of this VM.  # noqa: E501
        :type status: str
        :param can_ip_forward: The can_ip_forward of this VM.  # noqa: E501
        :type can_ip_forward: bool
        :param cpu_platform: The cpu_platform of this VM.  # noqa: E501
        :type cpu_platform: str
        :param deletion_protection: The deletion_protection of this VM.  # noqa: E501
        :type deletion_protection: bool
        :param disks: The disks of this VM.  # noqa: E501
        :type disks: List[DefinitionDISK]
        :param kind: The kind of this VM.  # noqa: E501
        :type kind: str
        :param label_fingerprint: The label_fingerprint of this VM.  # noqa: E501
        :type label_fingerprint: str
        """
        self.swagger_types = {
            'id': str,
            'creation_timestamp': datetime,
            'name': str,
            'description': str,
            'tags': VMTags,
            'machine_type': str,
            'status': str,
            'can_ip_forward': bool,
            'cpu_platform': str,
            'deletion_protection': bool,
            'disks': List[DefinitionDISK],
            'kind': str,
            'label_fingerprint': str
        }

        self.attribute_map = {
            'id': 'id',
            'creation_timestamp': 'creationTimestamp',
            'name': 'name',
            'description': 'description',
            'tags': 'tags',
            'machine_type': 'machineType',
            'status': 'status',
            'can_ip_forward': 'canIpForward',
            'cpu_platform': 'cpuPlatform',
            'deletion_protection': 'deletionProtection',
            'disks': 'disks',
            'kind': 'kind',
            'label_fingerprint': 'labelFingerprint'
        }

        self._id = id
        self._creation_timestamp = creation_timestamp
        self._name = name
        self._description = description
        self._tags = tags
        self._machine_type = machine_type
        self._status = status
        self._can_ip_forward = can_ip_forward
        self._cpu_platform = cpu_platform
        self._deletion_protection = deletion_protection
        self._disks = disks
        self._kind = kind
        self._label_fingerprint = label_fingerprint

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VM of this VM.  # noqa: E501
        :rtype: VM
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this VM.


        :return: The id of this VM.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VM.


        :param id: The id of this VM.
        :type id: str
        """

        self._id = id

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this VM.


        :return: The creation_timestamp of this VM.
        :rtype: datetime
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this VM.


        :param creation_timestamp: The creation_timestamp of this VM.
        :type creation_timestamp: datetime
        """

        self._creation_timestamp = creation_timestamp

    @property
    def name(self):
        """Gets the name of this VM.


        :return: The name of this VM.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VM.


        :param name: The name of this VM.
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this VM.


        :return: The description of this VM.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VM.


        :param description: The description of this VM.
        :type description: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this VM.


        :return: The tags of this VM.
        :rtype: VMTags
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VM.


        :param tags: The tags of this VM.
        :type tags: VMTags
        """

        self._tags = tags

    @property
    def machine_type(self):
        """Gets the machine_type of this VM.


        :return: The machine_type of this VM.
        :rtype: str
        """
        return self._machine_type

    @machine_type.setter
    def machine_type(self, machine_type):
        """Sets the machine_type of this VM.


        :param machine_type: The machine_type of this VM.
        :type machine_type: str
        """

        self._machine_type = machine_type

    @property
    def status(self):
        """Gets the status of this VM.


        :return: The status of this VM.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VM.


        :param status: The status of this VM.
        :type status: str
        """
        allowed_values = ["PROVISIONING", "STAGING", "RUNNING", "STOPPING", "STOPPED", "SUSPENDING", "SUSPENDED", "TERMINATED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def can_ip_forward(self):
        """Gets the can_ip_forward of this VM.


        :return: The can_ip_forward of this VM.
        :rtype: bool
        """
        return self._can_ip_forward

    @can_ip_forward.setter
    def can_ip_forward(self, can_ip_forward):
        """Sets the can_ip_forward of this VM.


        :param can_ip_forward: The can_ip_forward of this VM.
        :type can_ip_forward: bool
        """

        self._can_ip_forward = can_ip_forward

    @property
    def cpu_platform(self):
        """Gets the cpu_platform of this VM.


        :return: The cpu_platform of this VM.
        :rtype: str
        """
        return self._cpu_platform

    @cpu_platform.setter
    def cpu_platform(self, cpu_platform):
        """Sets the cpu_platform of this VM.


        :param cpu_platform: The cpu_platform of this VM.
        :type cpu_platform: str
        """

        self._cpu_platform = cpu_platform

    @property
    def deletion_protection(self):
        """Gets the deletion_protection of this VM.


        :return: The deletion_protection of this VM.
        :rtype: bool
        """
        return self._deletion_protection

    @deletion_protection.setter
    def deletion_protection(self, deletion_protection):
        """Sets the deletion_protection of this VM.


        :param deletion_protection: The deletion_protection of this VM.
        :type deletion_protection: bool
        """

        self._deletion_protection = deletion_protection

    @property
    def disks(self):
        """Gets the disks of this VM.


        :return: The disks of this VM.
        :rtype: List[DefinitionDISK]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this VM.


        :param disks: The disks of this VM.
        :type disks: List[DefinitionDISK]
        """

        self._disks = disks

    @property
    def kind(self):
        """Gets the kind of this VM.


        :return: The kind of this VM.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this VM.


        :param kind: The kind of this VM.
        :type kind: str
        """

        self._kind = kind

    @property
    def label_fingerprint(self):
        """Gets the label_fingerprint of this VM.


        :return: The label_fingerprint of this VM.
        :rtype: str
        """
        return self._label_fingerprint

    @label_fingerprint.setter
    def label_fingerprint(self, label_fingerprint):
        """Sets the label_fingerprint of this VM.


        :param label_fingerprint: The label_fingerprint of this VM.
        :type label_fingerprint: str
        """

        self._label_fingerprint = label_fingerprint
