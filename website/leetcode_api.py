import leetcode

leetcode_session = "yyy"
csrf_token = "xxx"

# Experimental: Or CSRF token can be obtained automatically
import leetcode.auth
csrf_token = leetcode.auth.get_csrf_cookie(leetcode_session)

configuration = leetcode.Configuration()

configuration.api_key["x-csrftoken"] = csrf_token
configuration.api_key["csrftoken"] = csrf_token
configuration.api_key["LEETCODE_SESSION"] = leetcode_session
configuration.api_key["Referer"] = "https://leetcode.com"
configuration.debug = False

api_instance = leetcode.DefaultApi(leetcode.ApiClient(configuration))

graphql_request = leetcode.GraphqlQuery(
    query="""
      {
        user {
          username
          isCurrentUserPremium
        }
      }
    """,
    variables=leetcode.GraphqlQueryVariables(),
)

print(api_instance.graphql_post(body=graphql_request))

# Output: