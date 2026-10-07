import type { ConfigType } from '@plone/registry';

import { searchBlocks } from './actions/searchBlocks';
import searchBlocksReducer from './reducers/searchBlocks';
import SearchBlocks from './components/SearchBlocks/SearchBlocks';
import ToolbarUserMenu from './components/manage/toolbar/ToolbarUserMenu';

function applyConfig(config: ConfigType) {
  config.addonReducers = {
    ...config.addonReducers,
    searchBlocks: searchBlocksReducer,
  };

  config.addonRoutes = [
    ...(config.addonRoutes || []),
    {
      path: '/controlpanel/search-blocks',
      component: SearchBlocks,
    },
  ];
  config.settings.appExtras = [
    ...config.settings.appExtras,
    {
      match: '',
      component: ToolbarUserMenu,
      props: {},
    },
  ];

  return config;
}

export default applyConfig;
export { searchBlocks };
