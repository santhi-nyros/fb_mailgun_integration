<?php
echo "sample";

$challenge = $_REQUEST['hub_challenge'];
$verify_token = $_REQUEST['hub_verify_token'];

if ($verify_token == '<YOUR_VERIFY_TOKEN>'){
	echo $challenge;
}

$fh = fopen('test.log', 'a+');
$input = json_decode(file_get_contents('php://input'));
fwrite($fh, print_r($input,true));

$frm_id  = $input->entry[0]->changes[0]->value->form_id;
fwrite($fh, $frm_id);



$auth = curl_init("<YOUR_APP_URL>/".$frm_id);
curl_setopt($auth, CURLOPT_HEADER, false);
curl_setopt($auth, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($auth);
curl_close($auth);

