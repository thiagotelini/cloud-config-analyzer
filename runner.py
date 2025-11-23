from utils.log_colors import CYAN, DEFAULT
from utils.display_response import pretty_print
from utils.html_report_generator import generate_html_report
from model.data_set_generator import data_set_generator
from model.train_model import train_model
from analyzer.configurations_analyzer import analyze

print(CYAN + 'Generating data for model training' + DEFAULT)
data_set_generator()

print(CYAN + 'Training model' + DEFAULT)
model = train_model()

print(CYAN + 'Model predicting' + DEFAULT)
response = analyze(model)

generate_html_report(response)
pretty_print(response)