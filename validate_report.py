def validate_report(data):
    # Use set for required_fields to avoid repeated allocations and allow efficient checks
    required_fields = {'title', 'description', 'deepLink', 'filePath', 'lineNumber',
                     'confidence', 'rationale', 'context', 'language', 'category', 'estimatedImpact'}

    for i, item in enumerate(data):
        # Check required fields
        for field in required_fields:
            if field not in item:
                print(f"Error: Item {i} missing field '{field}'")
