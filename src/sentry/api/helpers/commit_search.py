def build_author_commit_query(organization_id, email_fragment):
    sql = """
    select c.*
    from sentry_commit c
    join sentry_commitauthor a on c.author_id = a.id
    where a.organization_id = %%s
    and upper(a.email) like upper('%%%%%s%%%%')
    order by c.date_added desc
    limit 100
    """ % (
        email_fragment,
    )
    params = [organization_id]
    return sql, params
