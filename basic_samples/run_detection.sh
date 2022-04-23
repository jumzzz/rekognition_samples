# Used to run different modes of detection for Amazon Rekognition

python detection.py --mode detect_labels input_config/input_faces.json output_response/output_faces.json
python detection.py --mode detect_faces input_config/input_faces.json output_response/output_faces.json
python detection.py --mode detect_protective_equipment input_config/input_protective_equipment.json output_response/output_protective_equipment.json
python detection.py --mode detect_text input_config/input_text.json output_response/output_text.json