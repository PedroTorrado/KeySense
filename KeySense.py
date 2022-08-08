import sys
import pygame.midi
from pygame import midi

midi.init()

midi_input = midi.Input(midi.get_default_input_id())

default_id = midi.get_default_input_id()

pygame.midi.init()

print("Diagnostics -------------")
print(f"MIDI Device Connected: {pygame.midi.get_init()}")
print(f"Number of MIDI Devices Connected: {pygame.midi.get_count()}")
for i in range(pygame.midi.get_count()):
    print(pygame.midi.get_device_info(i), i)
print("--------------------------")

while True:
    pygame.midi.Input.poll(midi_input)
    midi_data = pygame.midi.Input.read(midi_input, 1)
    midi_note, timestamp = midi_data[0]
    note_status, keynum, velocity, unused = midi_note
    print("Midi Note: \n\tNote Status: ", note_status, " Key Number: ", keynum," Velocity: " , velocity, "\n\tTime Stamp: ", timestamp)
