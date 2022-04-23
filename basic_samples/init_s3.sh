echo "Creating S3 Bucket s3://rekognition-input-images"
aws s3 mb s3://rekognition-input-images

echo "Copying input_data/ to s3://rekognition-input-images/input_data/ recursively"
aws s3 cp input_data/ s3://rekognition-input-images/input_data --recursive