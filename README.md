# Tests-for-enum_oblako
Tests for https://github.com/lisp3r/enum_oblako

## Payload

All test files are generated on bb2bbd81c10be8b66c2397d558faba9db55c25a1 commit for 'test' name with `--generate` flag.

1. `generate_mutations.txt` - mutations
2. `enum_saas.txt` - payload from `saas_urls`.
3. `enum_buckets.txt` - payload from `bucket_urls`
4. `enum_buckets_with_namespaces.txt` - payload from `namespaces_urls`.
5. `enum-urls-for-test.txt` - all the urls to test `generate_enum_payload()` function.

## Run

```shell
$ cd enum_oblako
$ git clone https://github.com/lisp3r/Tests-for-enum_oblako.git tests
$ pytest tests
```
