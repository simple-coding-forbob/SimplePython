PUT /filedb-likes
{
  "mappings": {
    "properties": {
      "id": { "type": "long" },
      "email": { "type": "keyword" },
      "uuid": { "type": "keyword" },
      "like_count": { "type": "long" },
      "file_title": { "type": "text",
                    "fields": { "keyword": { "type": "keyword" } } },
      "file_content": { "type": "text" },
      "file_url": { "type": "keyword" },
      "name": { "type": "keyword" },
      "insert_time": { "type": "date" },
      "update_time": { "type": "date" }
    }
  }
}

PUT /filedb-likes-suggested
{
  "mappings": {
    "properties": {
      "email": { "type": "keyword" },
      "suggested": { "type": "keyword" },
      "insert_time": { "type": "date" },
      "update_time": { "type": "date" }
    }
  }
}

PUT /gallery-likes
{
  "mappings": {
    "properties": {
      "id": { "type": "long" },
      "email": { "type": "keyword" },
      "uuid": { "type": "keyword" },
      "like_count": { "type": "long" },
      "gallery_title": { "type": "text",
                    "fields": { "keyword": { "type": "keyword" } } },
      "gallery_url": { "type": "keyword" },
      "name": { "type": "keyword" },
      "insert_time": { "type": "date" },
      "update_time": { "type": "date" }
    }
  }
}


PUT /gallery-likes-suggested
{
  "mappings": {
    "properties": {
      "email": { "type": "keyword" },
      "suggested": { "type": "keyword" },
      "insert_time": { "type": "date" },
      "update_time": { "type": "date" }
    }
  }
}