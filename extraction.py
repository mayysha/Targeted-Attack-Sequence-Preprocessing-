import csv

def get_data_text():
    sequences_csv = "/content/drive/MyDrive/DPL2/Isequences.csv"
    data_text = []
    with open(sequences_csv, "r", newline="") as read_file:
        sequence_reader = csv.reader(read_file)
        for sequence in sequence_reader:
            data_text.append(sequence)
    return data_text

def sequence_to_indices(data_text, step_to_index):
    data_index = []

    for sequence in data_text:
        step_indices = []
        for step in sequence:
            step_indices.append(step_to_index[step])
        data_index.append(step_indices)

    return data_index

def get_conversion_dicts():

    # create dicts for step_to_index conversion and vice-versa
    unique_steps_filepath = "/content/drive/MyDrive/DPL2/unique_steps.txt"

    step_to_index = {}
    index_to_step = {}

    with open(unique_steps_filepath, "r") as read_file:
        lines = read_file.readlines()

        for idx, line in enumerate(lines):
            line = line.strip()     
            idx += 1    # will start indexing from 1
            step_to_index[line] = idx
            index_to_step[idx] = line

    return step_to_index, index_to_step


def get_train_test_data(train_indices, test_indices):

    sequences_csv = "/content/drive/MyDrive/DPL2/Isequences.csv"
    train_data_sequence = []
    test_data_sequence = []

    with open(sequences_csv, "r", newline="") as read_file:
        sequence_reader = csv.reader(read_file)
        index = 0
        for sequence in sequence_reader:
            if index in test_indices:
                test_data_sequence.append(sequence)
            elif index in train_indices:
                train_data_sequence.append(sequence)
            index += 1

    return train_data_sequence, test_data_sequence
