"""
Neurolixir — a lightweight rule-based chat utility.

This module loads simple Q=A pairs from a 'gpt.txt' file,
performs fuzzy matching (via difflib.SequenceMatcher) to
find the best reply for a given input, and can optionally
speak replies using pyttsx3. It also exposes utility functions
to inspect and modify the in-memory dialogue store, and provides
interfaces to interact with external chat APIs (OpenAI, DeepSeek, and custom URLs).

Usage:
    - chat(text, output=True) -> Returns matched answer or None.
    - add_dialogue(question, answer, add_to_gpt_file=True) -> Adds new pair.
    - start_chat() -> Simple REPL loop for interactive chatting.
    - api.openai(api_key, question, model="gpt-3.5-turbo", temperature=0.7, system_prompt="You are my friend") -> str
    - api.deepseek(api_key, question, model="deepseek-chat", temperature=0.7, system_prompt="You are my friend") -> str
    - api.url(url, question, model="gpt-3.5-turbo", temperature=0.7, system_prompt="You are my friend") -> str
"""
from difflib import SequenceMatcher
import pyttsx3
import os
import time
from .api import _api
from .ctime import _TimeCalculator

class ChatFileError(Exception):
    """Raised when the dialogue source file cannot be read."""
    pass

def similarity(text1: str, text2: str) -> float:
    """
    Compute a similarity percentage between two strings.

    Returns:
        float: similarity in percent (0.0 - 100.0)
    """
    similarity_percent = SequenceMatcher(None, text1, text2).ratio() * 100
    return similarity_percent

# Load dialogues from gpt.txt in the same directory as this module.
# The file is expected to contain lines in the format: question=answer
try:
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gpt.txt')
    with open(path, encoding='utf-8') as file:
        content = file.read().split('\n')
        dialogue = {}
        for item in content:
            lines = item.strip().split('=')
            if len(lines) >= 2:
                question = lines[0].strip()
                answer = lines[1].strip()
                dialogue[question] = answer
except FileNotFoundError:
    print(f'Chat file path: {path}')
    raise ChatFileError(
        "The 'gpt.txt' file was not found.")
except Exception as e:
    print(f'Chat file path: {path}')
    raise ChatFileError(
        f"An error occurred while reading 'gpt.txt': \n{e}")

def chat(text: str, output: bool =False, begin: str ='', speak: bool =False,
         invalid_message: str ='Please input valid content', end: str ='') -> str | None:
    """
    Find the best matching question for the given text and return its answer.

    Args:
        text (str): input text to match against stored questions.
        output (bool): if True, print the answer to stdout.
        begin (str): prefix to print before the answer when output=True.
        speak (bool): if True, use pyttsx3 to speak the answer.
        invalid_message (str): message to show/speak when no match is found.

    Returns:
        str or None: the matched answer, or None if no suitable match exists.
    """
    max_sim = 0
    best_q = None
    for question in dialogue:
        sim = similarity(text, question)
        if sim > max_sim:
            max_sim = sim
            best_q = question
    if best_q:
        ans = dialogue[best_q]
        if ans == 'time':
            ans = str(time.ctime())
        if output:
            print(f'{begin}{ans}{end}')
        if speak:
            pyttsx3.speak(f'{begin}{ans}{end}')
        return ans
    else:
        # Speak the invalid message only if speak=True, otherwise just print.
        pyttsx3.speak(invalid_message) if speak else None
        print(f'{begin}{invalid_message}')
        return None

def add_dialogue(question: str, answer: str, add_to_gpt_file: bool =False):
    """
    Add a new question->answer pair to the in-memory dialogue store.

    If add_to_gpt_file is True the pair will be appended to 'gpt.txt' for persistence.
    """
    dialogue[question] = answer
    if add_to_gpt_file:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gpt.txt')
        with open(path, 'a', encoding='utf-8') as file:
            file.write(f'\n{question}={answer}')

def delete_dialogue(question: str, add_to_gpt_file: bool =False) -> str:
    """
    Delete a question->answer pair from the in-memory dialogue store.

    If the question does not exist, this function does nothing.
    """
    if isinstance(dialogue, dict) and question not in dialogue:
        raise KeyError(f'Question "{question}" not found in dialogue store.')
    if question in dialogue:
        del dialogue[question]
    if add_to_gpt_file:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gpt.txt')
        with open(path, 'w', encoding='utf-8') as file:
            for q, a in dialogue.items():
                file.write(f'{q}={a}\n')
    return question

def question_in_dialogue(question: str) -> bool:
    """
    Check whether a question (or a close match) exists in the dialogue store.

    This call uses the chat() fuzzy-matching behavior — it returns True if
    chat(question) returns a non-None result.
    """
    return chat(question) != None

def get_dialogue() -> dict:
    """Return the internal dialogue mapping (question -> answer)."""
    return dialogue

def questions_list() -> list:
    """Return a list of all stored questions."""
    return list(dialogue.keys())

def answers_list() -> list:
    """Return a list of all stored answers."""
    return list(dialogue.values())

def start_chat(speak: bool =False, Chinese: bool =False):
    """
    Start a simple interactive chat REPL.

    Args:
        speak (bool): if True, use TTS for replies.
        Chinese (bool): if True, display Chinese prompts/messages.
    """
    print('Start chatting! Type "exit" or "quit" to leave.' if not Chinese else '开始聊天吧!输入"exit"或"quit"退出')
    try:
        while True:
            user_input = input("You: " if not Chinese else "你: ")
            if user_input.lower() in ['exit', 'quit', '退出', '离开', 'bye', '再见']:
                break
            chat(user_input, output=True, begin='Neurolixir: ', speak=speak)
        raise RuntimeError("Chat ended by user.")
    except (KeyboardInterrupt, RuntimeError):
        bye = "Chat ended by user."
        print(f'Neurolixir: {bye}')
        pyttsx3.speak(bye) if speak else None

api = _api()
TimeCalculator = _TimeCalculator()