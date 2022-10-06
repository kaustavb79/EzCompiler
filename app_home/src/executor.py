import subprocess
import logging
from django.core.files.storage import default_storage
from django.http import HttpResponse, JsonResponse
import os
import json
from django.conf import settings

logger = logging.getLogger('ez_compiler')

def write_to_file(file_path, code):
    # Write to empty file
    if file_path:
        try:
            print("11111111111111111111111111111111111111111")
            with open(file_path, 'w') as codefile:
                codefile.write(code)
            print("File write completed : ", file_path)
            # if language=='java':
            #     if os.path.exists(temp_file.replace('java', 'class')):
            #         print("File exist : ", temp_file.replace('java', 'class'))
            #         command = command + ";java " + temp_file.replace('java', '')
        except Exception as e:
            print("File write failed : ", file_path, "\n\n", e)


# compile code
def execute(code, stdin, language, class_name):
    # candidate_id = request.user.profile.user_uuid
    # q_id = request.POST['q_id']
    # file = request.FILES['code_file']
    # file_name = file.name
    # language = request.POST['language']
    # class_name = request.POST['class_name']

    print("---code---", code)
    print("---stdin---", stdin)
    print("---language---", language)
    print("---class_name---", class_name)

    # coding_response_path = request.POST['coding_response_path'].replace('media/', '')
    # print(request.FILES)
    # coding_response_path = 'coding_responses/on_demand/JOB_1a77771d-0e11-46fa-8092-c9fe21c0fd45/CND_03c36d90-67f9-4fe3-ab22-0f8fb17e43c6/Q_975427fc-27b2-485c-b6a8-3e34ffccf484'

    relative_code_path = '/media/web/'
    full_coding_dir = os.getcwd() + relative_code_path
    # os.path.join('coding_responses',
    #                                     os.path.join('on_demand', os.path.join(job_id, os.path.join(
    #                                         candidate_id, q_id))))
    print('full_coding_dir', full_coding_dir)

    # absolute_folder_path = os.getcwd() + '/media/' + coding_response_path
    # absolute_folder_path = full_coding_dir

    file_name = 'temp'
    if language == 'java':
        # full_file_path = default_storage.save(relative_code_path + class_name + '.' + language, code)
        full_file_path = full_coding_dir + class_name + '.' + language
        write_to_file(full_file_path, code)
        file_base_name = full_file_path.replace(full_coding_dir, '').replace('.' + language, '')
        absolute_file_path = full_file_path
        # absolute_file_path = os.getcwd() + '/media/' + path
        # file_folder = absolute_file_path.split(class_name)[0]
        # file_folder = coding_response_path + '/'
    else:
        # full_file_path = default_storage.save(relative_code_path + file_name + '.' + language, code)
        full_file_path = full_coding_dir + file_name + '.' + language
        write_to_file(full_file_path, code)

        file_base_name = full_file_path.replace(full_coding_dir, '').replace('.' + language, '')
        absolute_file_path = full_file_path
        # absolute_file_path = os.getcwd() + '/media/' + path
        # file_folder = absolute_file_path.split(file_name)[0]
        # file_folder = coding_response_path + '/'
    language = language
    if language == 'py':
        command = "cd " + full_coding_dir + " && python " + absolute_file_path
    elif language == 'py3':
        command = "cd " + full_coding_dir + " && python3 " + absolute_file_path
    elif language == 'java':
        print("-------", full_coding_dir, "---", file_base_name)
        command = "cd " + full_coding_dir + " && javac " + file_base_name + '.java' + " && " + 'java ' + file_base_name
    elif language == 'cpp':
        command = 'cd ' + full_coding_dir + ' && g++ ' + file_base_name + '.cpp -o ' + full_coding_dir + file_base_name + ' && ' + full_coding_dir + file_base_name
    elif language == 'c':
        command = 'cd ' + full_coding_dir + ' && g++ ' + file_base_name + '.c -o ' + full_coding_dir + file_base_name + ' && ' + full_coding_dir + file_base_name
    elif language == 'c#':
        command = 'cd ' + full_coding_dir + ' && csc ' + file_base_name + '.cs -o ' + full_coding_dir + file_base_name + ' && ' + full_coding_dir + file_base_name
    elif language == 'r':
        command = 'cd ' + full_coding_dir + ' && Rscript ' + file_base_name + '.r'
    elif language == 'rb':
        command = 'cd ' + full_coding_dir + ' && ruby ' + file_base_name + '.rb'
    elif language == 'js':
        pass
    else:
        command = "python3 " + absolute_file_path

    print("Command : ", command)
    if language == 'js':
        response_dict = {
            'run_result': 'success'
        }
    else:
        try:
            # output = subprocess.check_output(
            #     command, stderr=subprocess.STDOUT, shell=True, timeout=30,
            #     universal_newlines=True)
            print("command : ", command)
            p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, stdin=subprocess.PIPE)
            p.stdin.write(str.encode(stdin))
            (output, err) = p.communicate()
            p.stdin.close()
            output = output.decode("utf-8")
            output = output.replace(full_coding_dir, '')
            print("Output : ", output)
        except subprocess.CalledProcessError as exc:
            print("Status : FAIL", exc.returncode, exc.output)
            output = exc.output
            # directory_path = absolute_file_path.replace(file_name+'.'+''+, '')
            output = output.replace(absolute_file_path.split(file_name)[0], '').replace(file_name, 'yourfile')
        message = 'success'
        response_dict = {
            'message': message,
            'run_result': str(output)
        }
    return output


def get_language_compiler_version(lang):
    print("lang ",lang)
    status = "failure"
    message = "Invalid language/extension specified!!"
    command = ""
    if lang == 'py3':
        command = "python3 --version"
    elif lang == 'py2':
        command = "python2 --version"
    elif lang == 'java':
        command = "javac --version"
    elif lang == 'c':
        command = "gcc --version"
    elif lang == 'cpp':
        command = "g++ --version"
    elif lang == 'sql':
        command = "mysql --version"
    
    try:
        logger.info(" command : %s", command)
        output = subprocess.check_output(
            command, stderr=subprocess.STDOUT, shell=True, timeout=30,
            universal_newlines=True)
        print("Output : ", output)
    except subprocess.CalledProcessError as exc:
        logger.exception("Exception occurred when executing 'get_language_compiler_version'!!!")
        print("Status : FAIL", exc.returncode, exc.output)
        output = exc.output
    else:
        status="success"
        message = "Version Fetch call completed..."
    
    json_response = {
        "status":status,
        "message":message,
        "output":output,
    }
    
    return json_response
