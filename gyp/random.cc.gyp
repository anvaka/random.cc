{
  'includes': [
    './common.gypi'
  ],
  'targets': [{
      'target_name': 'random',
      'type': 'none',
      'sources': [ ],
      'include_dirs': [
          '../include'
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '../include'
        ],
      },
    },
  ]
}
