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



class MainHandler(webapp2.RequestHandler):
    def get(self):

        header = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Signup</title>
        </head>
        <body>
        """

        footer = """
        </body>
        </html>
        """

        # TODO 1: Create a form that asks for the following:
        #   1. Name
        #   2. Password
        #   3. Password Verify
        #   4. E-mail (optional)
        # And posts to a validation handler
        body = "Signup page"

        # TODO 3: Check for and display error
        error = self.request.get("error")

        content = header + body + footer
        self.response.write(content)

class SignupHandler(webapp2.RequestHandler):
    def post(self):

        # TODO 2: Validate the user's input
        #   - If valid, redirect to welcome page
        #   - If invalid, redirect back to main page and send an error message
        self.response.write('Welcome page')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', SignupHandler)
], debug=True)
