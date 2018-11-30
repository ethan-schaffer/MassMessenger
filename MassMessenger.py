# coding: utf-8
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import random
import pprint

pp = pprint.PrettyPrinter(indent=4)
import requests

import urllib2
import ssl

file_phone_numbers = open("file_phone_numbers", "r")
# This file is not on GitHub for security reasons

phone_numbers = {}
for line in file_phone_numbers:
    number = line.split(" ")[0]
    rest = ['']
    if len(line.split(" ")) > 1:
        rest = line.split()[1:]
    phone_numbers[number] = rest
    
base_url = 'https://dog.ceo/api/'


def _get(resource):
    url = '{0}{1}'.format(base_url, resource)
    # print("    Getting from url: " + url)
    res = requests.get(url)
    res = urllib2.urlopen(url, context=ssl._create_unverified_context()).read()
    # print("    Res =  " + str(res))
    content = res[31:-2].replace("", "")
    # print("    " + content)
    return content


def random_image(breed=None, subbreed=None):
    if breed is None and subbreed is None:
        return _get('breeds/image/random')
    elif subbreed is None:
        return _get('breed/{0}/images/random'.format(breed))
    else:
        return _get('breed/{0}/{1}/images/random'.format(breed, subbreed))


simple_breeds = [
    "affenpinscher", "african", "airedale",
    "akita", "appenzeller", "basenji", "beagle",
    "bluetick", "borzoi", "bouvier", "boxer",
    "brabancon", "briard", "cairn", "chihuahua",
    "chow", "clumber", "cockapoo", "coonhound",
    "cotondetulear", "dachshund", "dalmatian",
    "dhole", "dingo", "doberman", "entlebucher",
    "eskimo", "germanshepherd", "groenendael",
    "husky", "keeshond", "kelpie", "komondor",
    "kuvasz", "labrador", "leonberg", "lhasa",
    "malamute", "malinois", "maltese", "mexicanhairless",
    "newfoundland", "otterhound", "papillon", "pekinese",
    "pembroke", 'pug', 'puggle', "rottweiler", "saluki", "samoyed",
    "schipperke", "shiba", "shihtzu", "stbernard", "vizsla",
    "weimaraner", "whippet"]
complex_breeds = ['boston bulldog', 'french bulldog', 'staffordshire bullterrier',
                  'australian cattledog', 'border collie', 'cardigan corgi',
                  'great dane', 'scottish deerhound', 'norwegian elkhound',
                  'norwegian greyhound', 'afghan hound', 'basset hound', 'blood hound',
                  'english hound', 'ibizan hound', 'walker hound', 'bull mastiff',
                  'tibetan mastiff', 'bernese mountain', 'swiss mountain', 'miniature pinscher',
                  'german pointer', 'pomeranian pointer', 'miniature poodle',
                  'standard poodle', 'toy poodle',
                  'pyrenees poodle', 'redbone poodle', 'chesapeake retriever',
                  'curly retriever', 'flatcoated retriever', 'golden retriever',
                  'rhodesian ridgeback', 'giant schnauzer', 'miniature schnauzer',
                  'english setter', 'gordon setter', 'irish setter', 'english sheepdog',
                  'shetland sheepdog', 'blenheim spaniel', 'brittany spaniel', 'cocker spaniel',
                  'irish spaniel', 'japanese spaniel', 'sussex spaniel', 'welsh spaniel',
                  'english springer', 'american terrier', 'australian terrier', 'bedlington terrier',
                  'border terrier', 'dandie terrier', 'fox terrier', 'irish terrier',
                  'kerryblue terrier', 'lakeland terrier', 'norfolk terrier', 'norwich terrier',
                  'patterdale terrier', 'russell terrier', 'scottish terrier', 'sealyham terrier',
                  'silky terrier', 'tibetan terrier', 'toy terrier', 'westhighland terrier',
                  'wheaten terrier', 'yorkshire terrier', 'irish wolfhound']
general_breeds = ['cattledog', 'spaniel', 'greyhound', 'bullterrier',
                  'corgi', 'dane', 'springer', 'schnauzer', 'pinscher',
                  'poodle', 'ridgeback', 'deerhound', 'sheepdog', 'hound',
                  'mastiff', 'setter', 'collie', 'wolfhound', 'retriever',
                  'elkhound', 'bulldog', 'terrier', 'pointer', 'mountain']

puppies = []
file_puppies = open("file_puppies", "r")
for line in file_puppies:
    puppies.append(line)

cats = []
file_cats = open("file_cats", "r")
for line in file_cats:
    cats.append(line)

quokkas = []
file_quokkas = open("file_quokkas", "r")
for line in file_quokkas:
    quokkas.append(line)

babies = []
file_babies = open("file_babies", "r")
for line in file_babies:
    babies.append(line)

baby_requests = ["baby", "babies"]
cat_requests = ["kitten", "kitty", "cat"]


def process_request(request, used):
    words = request.lower()
    for breed in simple_breeds:
        if breed in words or breed in words.replace(" ", ""):
            choice = random_image(breed)
            while choice in used:
                choice = random_image(breed)
            return choice
    for full_breed in complex_breeds:
        if full_breed in words:
            breed = full_breed.split(" ")[0]
            species = full_breed.split(" ")[1]
            choice = random_image(species, breed)
            while choice in used:
                choice = random_image(species, breed)
            return choice
    for species in general_breeds:
        if species in words:
            breeds = [x for x in complex_breeds if species in x]
            choice = random_image(species, random.choice(breeds).split(" ")[0])
            while choice in used:
                choice = random_image(species, random.choice(breeds).split(" ")[0])
            return choice
    if "cat" in words:
        choice = random.choice(cats)
        while choice in used:
            choice = random.choice(cats)
        return choice
    if "quokka" in words:
        return random.choice(quokkas)
    if "baby" in words:
        choice = random.choice(babies)
        while choice in used:
            choice = random.choice(babies)
        return choice
    return None


account_sid = ""
file_account_sid = open("file_account_sid", "r")
# This file is not on GitHub for security reasons
for line in file_account_sid:
    account_sid = line

auth_token = ""
file_auth_token = open("file_account_sid", "r")
# This file is not on GitHub for security reasons
for line in file_auth_token:
    auth_token = line

client = Client(account_sid, auth_token)

admin = "+15129000311".encode("utf8")
past_sent = {}
for number in phone_numbers:
    past_sent[number] = []

total_requests = {}
good_numbers = [admin]

for number in phone_numbers:
    good_numbers.append(number)
    total_requests[number] = 0

need_verification = []

SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

failed_messages = []


@app.route("/", methods=['GET'])
def inbound_sms():
    global need_verification
    global past_sent
    from_number = request.values.get('From')
    text_body = request.values.get('Body')

    print("Message Recieved from: " + from_number + ".")
    print("Message reads: " + text_body)

    if from_number is admin:
        if text_body is "Random":
            message = client.messages.create(body="Message <number> " + random.choice(puppies),
                                             from_='+12109413835', to=admin)
            return "Gave Random"
        if text_body is "Send All":
            message_all_numbers()
            return "Sent all"
        if text_body is "Failed Logs":
            message = client.messages.create(body=str(failed_messages), from_='+12109413835', to=admin)
            return "Sent Failed Logs"
        if text_body.split(" ")[0] is "For":
            number = text_body.split(" ")[1]
            potential_images = []
            image = None
            tries = 0
            while image is None:
                tries += 1
                for entry in phone_numbers[number]:
                    potential_images.append(process_request(entry, past_sent[number]))
                image_set = [x for x in potential_images if x is not None]
                if len(image_set) > 0:
                    potential_image = random.choice(image_set)
                else:
                    potential_image = random.choice(puppies)
                image = potential_image
                if tries > 5:
                    message = client.messages.create(body="Took too many tries", from_='+12109413835', to=admin)
                    return ""
            message = client.messages.create(body="Message " + number + " " + image, from_='+12109413835', to=admin)
            return ""
        if text_body is "Reload All":
            for index in range(len(need_verification)):
                item = need_verification[index]
                print("Would send to " + str(item))
                number = item[0]
                need_verification[index][1] = process_request(str(phone_numbers[number]), past_sent[number])
            print("")
            for entry in need_verification:
                print(str(need_verification.index(entry)) + " " + str(entry))
            print("")
            return ""
        if text_body.split(" ")[0] is "Reload":
            index = int(text_body.split(" ")[1])
            item = need_verification[index]
            print("Would send to " + str(item))
            number = item[0]
            need_verification[index][1] = process_request(str(phone_numbers[from_number]), past_sent[number])
            print("")
            for entry in need_verification:
                print(str(need_verification.index(entry)) + " " + str(entry))
            print("")
            return ""

        if text_body is "Verify Done":
            need_verification = []
            print("Discarded remaining waiting numbers")
            return "All verified now"
        if text_body.split(" ")[0] is "Verify":
            if need_verification is []:
                print("Nothing to verify")
                return ""
            number = int(text_body.split(" ")[1])
            item = need_verification[number]
            print("Would send to " + str(item))
            image = item[1]
            number = item[0]
            message_text = item[3]
            print(image + " " + number)
            past_sent[number].append(image)
            message = client.messages.create(body=message_text, from_='+12109413835', media_url=image, to=number)
            need_verification.remove(item)
            print("")
            for entry in need_verification:
                print(str(need_verification.index(entry)) + " " + str(entry))
            print("")
            return "Verified"
        if text_body.split(" ")[0] is "Message":
            if len(text_body.split(" ")) == 3:
                number = text_body.split(" ")[1]
                link = text_body.split(" ")[2]
                if link.lower() is "random":
                    link = random.choice(puppies)
                past_sent[number].append(link)
                total_requests[number] += 1
                message = client.messages.create(body="", from_='+12109413835', media_url=link, to=number)
                return "Sent Message"
            if len(text_body.split(" ")) > 3:
                number = text_body.split(" ")[1]
                link = text_body.split(" ")[2]
                if link.lower() is "random":
                    link = random.choice(puppies)
                past_sent[number].append(link)
                total_requests[number] += 1
                message_body = " ".join(text_body.split(" ")[3:])
                message = client.messages.create(body=message_body, from_='+12109413835', media_url=link, to=number)
                return "Sent Message"
        if text_body is "Dump":
            pp.pprint(past_sent)
            return "Dumped"

    if from_number in good_numbers:
        print("This is request number " + str(total_requests[from_number]) + " from this person")
        if total_requests[from_number] <= 3 or from_number is admin:
            image = None
            while (image is None) or (image in past_sent[from_number]):
                image = process_request(text_body + " " + str(phone_numbers[from_number]), past_sent[from_number])
                if image is None:
                    for baby_request in baby_requests:
                        if baby_request in text_body.lower():
                            image = random.choice(list(set(babies) - set(past_sent[from_number])))
                if image is None:
                    print("Couldn't find solution, waiting for Admin")
                    print("Message: " + text_body)
                    print("Number: " + from_number)
                    failed_messages.append((text_body, from_number))
                    message = client.messages.create(
                        body="Failed Message: nNumber: " + from_number + "nBody: " + text_body + "\nNotes: " + str(
                            phone_numbers[from_number]), from_='+12109413835', to=admin)
                    message = client.messages.create(body="Message " + from_number + " " + random.choice(
                        list(set(puppies) - set(past_sent[from_number]))), from_='+12109413835', to=admin)
                    return ""
            print("Suggesting image reply: ")
            print("   " + image)
            print("")
            expected_message = "Message " + from_number + " " + image
            if from_number is not admin:
                message = client.messages.create(
                    body="Number: " + from_number + "nBody: " + text_body + "\nNotes: " + str(
                        phone_numbers[from_number]), from_='+12109413835', to=admin)
            message = client.messages.create(body=expected_message, from_='+12109413835', to=admin)
            return "Sent Message Suggestion to admin"
        else:
            message = client.messages.create(
                body="Past 3rd message from:nNumber: " + from_number + "nBody: " + text_body + "\nNotes: " + str(
                    phone_numbers[from_number]), from_='+12109413835', to=admin)
            print("Not going to reply, already reached max.")
    else:
        print("Not going to reply, this number is not a contact.")
    print("Processed Message------")
    return "Processed incoming message"


def message_all_numbers():
    global need_verification
    need_verification = []
    global past_sent
    for phone_number in phone_numbers:
        image = None
        valid_puppies = list(set(puppies) - set(past_sent[phone_number]))
        if len(valid_puppies) > 0:
            image = random.choice(valid_puppies)
        if phone_numbers[phone_number][0] not in ['', 'Special', 'Named']:
            potential_images = []
            for entry in phone_numbers[phone_number]:
                r = process_request(entry, past_sent[phone_number])
                potential_images.append(r)
            image_set = [x for x in potential_images if x is not None]
            potential_image = None
            if len(image_set) > 0:
                potential_image = random.choice(image_set)
            if potential_image is not None:
                image = potential_image
        message_text = random.choice(["Good morning!", "Good Morning!", "Have a great day!", "Have a Great Day!"])
        if phone_numbers[phone_number][0] is 'Special':
            image = process_request(str(phone_numbers[phone_number][1:]), past_sent[phone_number])
        if image in puppies or image in babies or image in quokkas or image in cats:
            if phone_number is not admin:
                past_sent[phone_number].append(image)
                print("Sent image " + image + " to " + phone_number + " with message " + message_text)

                message = client.messages.create(body=message_text, from_='+12109413835', media_url=image,
                                                 to=phone_number)
        else:
            if image is None:
                image = "<No Image Found>"
            print("   Considering image " + image + " to " + phone_number)
            need_verification.append([phone_number, image, str(phone_numbers[phone_number]), message_text])
    print("Messaged all numbers!")
    print("")
    dictionary = {}
    for entry in need_verification:
        dictionary[entry[0]] = []
    for entry in need_verification:
        dictionary[entry[0]].append(entry[1:])

    need_verification = []
    for (key, val) in dictionary.items():
        new_l = [key]
        new_l.extend(val[0])
        need_verification.append(new_l)

    for entry in need_verification:
        print(str(need_verification.index(entry)) + " " + str(entry))
    for phone_number in phone_numbers:
        total_requests[phone_number] = 0
    print("Requests set to 0")


if __name__ == "__main__":
    print("Program Running")
    app.run(host='0.0.0.0', debug=False)
