create table if not exists
    kv (
        key varchar(2048) primary key,
        value text not null
    );

create table if not exists
    schema(
        id bigserial primary key,
        value jsonb not null
    );

create table if not exists
    docs (
        key varchar(2048) primary key,
        schema_id bigint references schema(id) not null,
        value jsonb not null
    );

create table if not exists
    locker (
        key varchar(2048) primary key,
        is_locked boolean default false not null,
        table_name varchar(100)
    );
