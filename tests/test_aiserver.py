""" AI Server Tests
"""

import unittest
import os
from typing import List

from servicestack.clients import UploadFile
from .config import *
from .aiserver_dtos import SpeechToText, GenerationResponse


def create_aiserver_client():
    """Create a client for AI Server tests using environment variables"""
    url = os.getenv('AI_SERVER_URL')
    api_key = os.getenv('AI_SERVER_API_KEY')

    if not url or not api_key:
        raise EnvironmentError(
            "AI_SERVER_URL and AI_SERVER_API_KEY environment variables are required. "
            "Please set these before running the AI server tests."
        )

    client = JsonServiceClient(url)
    client.set_bearer_token(api_key)
    return client


class TestAiServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Skip all tests in this class unless explicitly running AI tests"""
        if not os.getenv('RUN_AI_TESTS'):
            raise unittest.SkipTest(
                "Skipping AI Server tests. Set RUN_AI_TESTS=1 to run these tests."
            )
        cls.client = create_aiserver_client()

    def test_can_speech_to_text(self):
        """Test speech to text functionality with file upload"""
        request = SpeechToText()

        # Open the test audio file in binary read mode
        with open("tests/files/test_audio.wav", "rb") as audio_file:
            upload = UploadFile(
                field_name="audio",
                file_name="test_audio.wav",
                content_type="audio/wav",
                stream=audio_file
            )

            # Send request with file
            response: GenerationResponse = self.client.post_files_with_request(
                request_uri="/api/SpeechToText",
                request=request,
                files=upload
            )

            # Verify response structure
            self.assertIsNotNone(response)
            self.assertTrue(hasattr(response, 'text_outputs'))
            self.assertIsInstance(response.text_outputs, List)
            self.assertEqual(len(response.text_outputs), 2)

            # Get both text outputs
            text_with_timestamps = response.text_outputs[1].text
            text_only = response.text_outputs[0].text

            # Basic validation of outputs
            self.assertIsNotNone(text_with_timestamps)
            self.assertIsNotNone(text_only)

            print("\nSpeech to Text Results:")
            print("Text with timestamps:", text_with_timestamps)
            print("Text only:", text_only)


if __name__ == '__main__':
    # When running this file directly, automatically set RUN_AI_TESTS
    os.environ['RUN_AI_TESTS'] = '1'
    unittest.main()