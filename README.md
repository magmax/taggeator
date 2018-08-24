# Description

From a file with a tag description format like:

```
apps:                                                                                                                                                                    
    - name: fubar
      url: http://example.org/fubar
      description: a fubar app
      tags:
      - foo1
      - bar1

    - name: foo
      url: http://example.org/foo
      description: a foo app
      tags:
      - foo1
      - foo2

    - name: bar
      url: http://example.org/bar
      description: a bar app
      tags:
      - bar1
      - bar2
```

Generates a new file after applying a template with the inverted file, that is,
a dict of tags with each app as a dict.
