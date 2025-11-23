def check_public_read(acl, iam_policy):
    for entry in acl:
        if entry.get("entity") == "allUsers" and entry.get("role") in ("READER", "WRITER", "OWNER"):
            return 1

    bindings = iam_policy.get("bindings", [])
    for binding in bindings:
        members = binding.get("members", [])
        if "allUsers" in members:
            return 1

    return 0


def check_acl_all_users(acl):
    for entry in acl:
        if entry.get("entity") == "allUsers":
            return 1
    return 0


def check_encryption(encryption_info):
    if not encryption_info:
        return 0

    if encryption_info.get("defaultKmsKeyName"):
        return 1

    if encryption_info.get("enabled") is True:
        return 1

    return 0


def adapt_bucket_config(bucket_json):
    bucket_name = bucket_json.get("name")
    acl = bucket_json.get("acl", [])
    iam_policy = bucket_json.get("iamPolicy", {})
    encryption_info = bucket_json.get("encryption")

    public_read = check_public_read(acl, iam_policy)
    acl_all_users = check_acl_all_users(acl)
    encryption = check_encryption(encryption_info)

    return {
        "bucket_name": bucket_name,
        "public_read": public_read,
        "encryption": encryption,
        "acl_all_users": acl_all_users
    }
