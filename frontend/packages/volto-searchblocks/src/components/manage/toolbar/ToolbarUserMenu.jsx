import React from 'react';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';

import { Icon } from '@plone/volto/components';
import rightArrowSVG from '@plone/volto/icons/right-key.svg';
import { Plug } from '@plone/volto/components/manage/Pluggable';

export const ToolbarUserMenu = () => {
  const searchBlocksAction = useSelector((state) =>
    (state.actions?.actions?.user ?? []).find(
      (action) => action.id === 'collective-searchblocks',
    ),
  );
  return searchBlocksAction ? (
    <Plug pluggable="toolbar-user-menu" id="collective-searchblocks-toolbar">
      <li>
        <Link
          to="/controlpanel/search-blocks"
          tabIndex={0}
          className="deleteBlocks"
          id="toolbar-search-blocks"
        >
          {searchBlocksAction.title} <Icon name={rightArrowSVG} size="24px" />
        </Link>
      </li>
    </Plug>
  ) : null;
};

export default ToolbarUserMenu;
