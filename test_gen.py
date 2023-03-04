import os

import enum_oblako

script_path = os.path.dirname(os.path.abspath(__file__))

namespaces = os.path.join(script_path, '..', 'namespaces.txt')
bucketnames = os.path.join(script_path, '..', 'bucketnames.txt')


def test_gen_mutations():
    mutations = enum_oblako.generate_mutations('test', enum_oblako.read_payload_file(namespaces))
    mutations.sort()

    test_mutations = os.path.join(script_path, 'generate_mutations.txt')
    mutations_etalon = enum_oblako.read_payload_file(test_mutations)

    assert len(mutations) == len(mutations_etalon)
    assert mutations == mutations_etalon


def test_gen_saas():
    mutations = enum_oblako.generate_mutations('test', enum_oblako.read_payload_file(namespaces))
    saas_urls = enum_oblako.enum_saas(mutations)
    saas_urls.sort()

    reference = enum_oblako.read_payload_file(os.path.join(script_path, 'enum_saas.txt'))

    assert len(saas_urls) == len(reference)
    assert saas_urls == reference


def test_gen_buckets():
    mutations = enum_oblako.generate_mutations('test', enum_oblako.read_payload_file(namespaces))
    buckets_urls = enum_oblako.enum_buckets(mutations)
    buckets_urls.sort()

    reference = enum_oblako.read_payload_file(os.path.join(script_path, 'enum_buckets.txt'))

    assert len(buckets_urls) == len(reference)
    assert buckets_urls == reference


def test_gen_buckets_and_namespaces():
    mutations = enum_oblako.generate_mutations('test', enum_oblako.read_payload_file(namespaces))
    s3_urls = enum_oblako.enum_buckets_with_namespaces(mutations, enum_oblako.read_payload_file(bucketnames))
    s3_urls.sort()

    reference = enum_oblako.read_payload_file(os.path.join(script_path, 'enum_buckets_with_namespaces.txt'))
    assert len(s3_urls) == len(reference)
    assert s3_urls == reference


def test_generate_enum_payload_func():
    mutations = enum_oblako.generate_mutations('test', enum_oblako.read_payload_file(namespaces))
    enum_urls = enum_oblako.generate_enum_payload(saas_payload=mutations, buckets_payload=mutations,
                                                  s3_buckets_payload=(
                                                      mutations, enum_oblako.read_payload_file(bucketnames)))

    reference = enum_oblako.read_payload_file(os.path.join(script_path, 'enum-urls-for-test.txt'))
    assert len(enum_urls) == len(reference)
    assert enum_urls == reference
