with DAG():
    SFTPSource_0 = SourceTask(
        task_id = "SFTPSource_0", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = XMLFormat(
          schema = {
            "fields": [{"dataType" : {"type" : "utf8"}, "name" : "@id"},                         {"dataType" : {"type" : "utf8"}, "name" : "author"},                         {"dataType" : {"type" : "utf8"}, "name" : "title"},                         {"dataType" : {"type" : "utf8"}, "name" : "genre"},                         {"dataType" : {"type" : "float64"}, "name" : "price"},                         {"dataType" : {"type" : "date32"}, "name" : "publish_date"},                         {"dataType" : {"type" : "utf8"}, "name" : "data_type"},                         {"dataType" : {"type" : "utf8"}, "name" : "description"}], 
            "providerType": "arrow"
          }
        ), 
        filePath = "/prophecy-sftp/aruns/book_catalog_with_types.xml"
    )
    SFTPSource_1 = SourceTask(
        task_id = "SFTPSource_1", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = XMLFormat(), 
        filePath = "/prophecy-sftp/aruns/complex_data_types_132123123.xml"
    )
    SFTPSource_2 = SourceTask(
        task_id = "SFTPSource_2", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = XMLFormat(
          schema = {
            "fields": [{"dataType" : {"type" : "utf8"}, "name" : "@type"},                         {"dataType" : {"dataType" : {"type" : "utf8"}, "type" : "Array"}, "name" : "Item"},                         {"dataType" : {"dataType" : {"type" : "utf8"}, "type" : "Array"}, "name" : "Field"}], 
            "providerType": "arrow"
          }
        ), 
        filePath = "/prophecy-sftp/aruns/complex_data_xml.xml"
    )
