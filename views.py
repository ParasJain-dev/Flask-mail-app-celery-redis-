def go_run(path_to_send,contest,question,path_to_question,compile_folder_path,code_language,name_of_file):
	startTime = datetime.now()
	testcase = Testcase.objects.filter(contest=contest,question=question)
	ans =0
	for testcase in testcase:
		print("gggg")
		name_out = testcase.outp.split('/')[-1]
		temp_out = '%s'%compile_folder_path + '/Output/%s'%name_out
		temp_out2 = '%s'%BASE_DIR + '%s'%testcase.inpt
		myinput = open(temp_out2)
		myoutput = open(temp_out,"w")
		print("paras",path_to_send)
		#subprocess.call('cd Contest',shell=True)
		cmd = ["java","-cp",path_to_send,name_of_file]
		#cmd = ["ls","-l"]
		out_testcase = '%s'%BASE_DIR + '%s'%testcase.outp
		compile_testcase = '%s'%compile_folder_path + '/Output/%s'%name_out
	#	print("this",out_testcase,compile_testcase)

		try:
			p = subprocess.run(cmd,timeout=.5,stdin=myinput,stdout = myoutput)
			if p.returncode==0:
				print("Successfully Compiled")
				ans = match_testcase_contest(out_testcase,compile_testcase,ans)
				if ans==0:
					break
			else:
				print("Error")
				ans=0
				break
		except subprocess.TimeoutExpired:
			print('Timeout',"hi")
			return HttpResponse("TLE Timeout",datetime.now() - startTime)
	if ans==0:
		return ans
	else:
		return ans


#check whether code is safe to run
def is_safe(input_check, language):
    input_check = input_check.lower()

    if 'python3' in language or 'python2' in language or 'Python3' in language or 'Python3' in language:
        if 'import os' in input_check or 'system(' in input_check or 'popen' in input_check or 'subprocess' in input_check:
            return False
        else:
            return True
    elif language == 'java' or language == 'Java':
        if '.getruntime(' in input_check or 'processbuilder(' in input_check:
            return False
        else:
            return True
    elif 'subprocess' in input_check or'fopen(' in input_check or 'open(' in input_check :
        return False
    return True
