with DAG():
    SFTPSource_0 = SourceTask(
        task_id = "SFTPSource_0", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = XMLFormat(
          schema = {
            "fields": [{"dataType" : {"type" : "int64"}, "name" : "id"},                         {"dataType" : {"type" : "utf8"}, "name" : "name"},                         {"dataType" : {"type" : "utf8"}, "name" : "email"},                         {"dataType" : {"dataType" : {"type" : "utf8"}, "type" : "Array"}, "name" : "item"}], 
            "providerType": "arrow"
          }
        ), 
        filePath = "/prophecy-sftp/aruns/sample_data.xml"
    )
