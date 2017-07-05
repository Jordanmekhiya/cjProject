#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2

jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader("templates"))

class MainHandler(webapp2.RequestHandler):
     def get(self):
        #this is where you reference your HTML file
        template = jinja_environment.get_template('hello.html')
        self.response.out.write(template.render({
            'template_name': self.request.get('name')
        }))

class PassHandler(webapp2.RequestHandler):
    def post(self):
        real_name = "Crystal"
        real_pass = "apples"
        username = self.request.get("username")
        password = self.request.get("password")
        self.response.write(username + " " + password)
        # if

class FormHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get('name')
        eyecolor = self.request.get('eyecolor')
        race = self.request.get('race')
        sex = self.request.get('sex')
        Password = self.request.get('Password')
        self.response.write(name + eyecolor + " " + race + " " + sex + " " + password)



#set up environment for Jinja
#this sets jinja's relative directory to match the directory name(dirname) of
#the current __file__, in this case, main.py


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/submission', FormHandler),
    ('/login', PassHandler)
], debug=True)
