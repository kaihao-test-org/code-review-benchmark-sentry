def lookup_release_file(manager, organization_id, file_id):
    return manager.get(id=file_id, release__organization_id=organization_id)
