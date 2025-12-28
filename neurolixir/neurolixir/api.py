import openai

class _api:
    def __init__(self):
        self.deepseek_com = 'https://api/deepseek.com/'

    def chat_openai(self, api: str, question: str ='What \'s your name?',
                    model: str='gpt-3.5-turbo', temperature=0.7,
                    system_prompt='You are my friend') -> str:
        """
        Delegate a chat request to the OpenAI-backed adapter.

        Args:
            api (str): API key or identifier used by chat_openai.
            question (str): The user prompt / question to send.
            model (str): Model identifier string.
            temperature (float): Sampling temperature.
            system_prompt (str): System-level instruction for the model.

        Returns:
            The response produced by chat_openai (format produced by that adapter).
        """
        openai.api_key = api
        messages = [
            {'role' : 'system', 'content' : system_prompt},
            {'role' : 'user', 'content' : question}
        ]
        response = openai.ChatCompletion.create(
            model=model, messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content

    def chat_deepseek(self, api: str, question: str ='What \'s your name?',
                    model: str='deepseek-chat', temperature=0.7,
                    system_prompt='You are my friend',
                    deepseek_com='https://api/deepseek.com') -> str:
        """
            Delegate a chat request to the Deepseek adapter.

            Args:
                api (str): API key or identifier used by chat_deepseek.
                question (str): The user prompt / question to send.
                model (str): Model identifier for Deepseek.
                temperature (float): Sampling temperature.
                system_prompt (str): System-level instruction for the model.
                deepseek_com (str): Base URL for the Deepseek API.

            Returns:
                The response produced by chat_deepseek.
        """
        client = openai.OpenAI(
            api_key=api, base_url=deepseek_com
        )
        openai.api_key = api
        messages = [
            {'role' : 'system', 'content' : system_prompt},
            {'role' : 'user', 'content' : question}
        ]
        response = client.chat.completions.create(
            model=model, messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content

    def chat_url(self, api: str, question: str ='What \'s your name?',
                    model: str='deepseek-chat', temperature=0.7,
                    system_prompt='You are my friend',
                    url='https://api/deepseek.com') -> str:
        """
            Delegate a chat request to a generic URL-based adapter.

            Args:
                api (str): API key or identifier.
                question (str): The user prompt / question to send.
                model (str): Model identifier (adapter-specific).
                temperature (float): Sampling temperature.
                system_prompt (str): System-level instruction for the model.
                url (str): Endpoint URL for the adapter.

            Returns:
                The response produced by chat_url.
        """
        client = openai.OpenAI(
            api_key=api, base_url=url
        )
        openai.api_key = api
        messages = [
            {'role' : 'system', 'content' : system_prompt},
            {'role' : 'user', 'content' : question}
        ]
        response = client.chat.completions.create(
            model=model, messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content