""" from https://github.com/keithito/tacotron """

from text import cleaners
from text.symbols import symbols


# Mappings from symbol to numeric ID and vice versa:
_symbol_to_id = {s: i for i, s in enumerate(symbols)}
_id_to_symbol = dict(enumerate(symbols))


def text_to_sequence(text, cleaner_names):
  '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
    Args:
      text: string to convert to a sequence
      cleaner_names: names of the cleaner functions to run the text through
    Returns:
      List of integers corresponding to the symbols in the text
  '''
  sequence = []

  clean_text = _clean_text(text, cleaner_names)
  for symbol in clean_text:
    if symbol not in _symbol_to_id.keys():
      continue
    symbol_id = _symbol_to_id[symbol]
    sequence += [symbol_id]
  return sequence


def cleaned_text_to_sequence(cleaned_text):
  '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
    Args:
      text: string to convert to a sequence
    Returns:
      List of integers corresponding to the symbols in the text
  '''
  return [
      _symbol_to_id[symbol] for symbol in cleaned_text
      if symbol in _symbol_to_id.keys()
  ]


def sequence_to_text(sequence):
  '''Converts a sequence of IDs back to a string'''
  return ''.join(_id_to_symbol[symbol_id] for symbol_id in sequence)


def _clean_text(text, cleaner_names):
  for name in cleaner_names:
    if cleaner := getattr(cleaners, name):
      text = cleaner(text)
    else:
      raise Exception(f'Unknown cleaner: {name}')
  return text
