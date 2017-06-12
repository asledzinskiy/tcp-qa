#    Copyright 2017 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations


from tcp_tests.managers.k8s.base import K8sBaseResource
from tcp_tests.managers.k8s.base import K8sBaseManager


class K8sReplicaSet(K8sBaseResource):
    """docstring for K8sPod"""

    def __repr__(self):
        return "<K8sPod: %s>" % self.name

    @property
    def name(self):
        return self.metadata.name


class K8sReplicaSetManager(K8sBaseManager):
    """docstring for ClassName"""

    resource_class = K8sReplicaSet

    def _get(self, name, namespace=None, **kwargs):
        namespace = namespace or self.namespace
        return self.api.read_namespaced_replica_set(
            name=name, namespace=namespace, **kwargs)

    def _list(self, namespace=None, **kwargs):
        namespace = namespace or self.namespace
        return self.api.list_namespaced_replica_set(namespace=namespace,
                                                    **kwargs)

    def _create(self, body, namespace=None, **kwargs):
        namespace = namespace or self.namespace
        return self.api.create_namespaced_replica_set(
            body=body, namespace=namespace, **kwargs)

    def _replace(self, body, name, namespace=None, **kwargs):
        namespace = namespace or self.namespace
        return self.api.replace_namespaced_replica_set(
            body=body, name=name, namespace=namespace, **kwargs)

    def _delete(self, body, name, namespace=None, **kwargs):
        namespace = namespace or self.namespace
        return self.api.delete_namespaced_replica_set(
            body=body, name=name, namespace=namespace, **kwargs)

    def _deletecollection(self, namespace=None, **kwargs):
        namespace = namespace or self.namespace
        return self.api.deletecollection_namespaced_replica_set(
            namespace=namespace, **kwargs)

    def full_list(self, *args, **kwargs):
        lst = self._full_list(*args, **kwargs)
        return [self.resource_class(self, item) for item in lst.items]

    def _full_list(self, **kwargs):
        return self.api.list_replica_set(**kwargs)
