from mongoengine import connect, Document, StringField, ValidationError

def test_connection():
    try:
        # Attempt to connect to MongoDB
        connect('testdb', host='localhost', port=27017)

        # Define a test document
        class TestDocument(Document):
            name = StringField(required=True)
            value = StringField()

        # Create and save a test document
        doc = TestDocument(name='connection_test', value='Connection successful')
        doc.save()

        # Query the document to verify
        result = TestDocument.objects(name='connection_test').first()
        if result:
            print(f'Connection successful! Document found: Name={result.name}, Value={result.value}')
        else:
            print('Connection successful but document not found.')

    except Exception as e:
        print(f'Failed to connect to MongoDB. Error: {e}')

if __name__ == "__main__":
    test_connection()
