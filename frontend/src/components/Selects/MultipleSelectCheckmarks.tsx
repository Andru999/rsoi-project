import OutlinedInput from '@mui/material/OutlinedInput';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import ListItemText from '@mui/material/ListItemText';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import Checkbox from '@mui/material/Checkbox';


interface MultipleSelectCheckmarksProps {
  label: string
  selectionList: string[]
	values: string[]
	setValues: (values: string[]) => void
}

const ITEM_HEIGHT = 48;
const ITEM_PADDING_TOP = 8;
const MenuProps = {
  PaperProps: {
    style: {
      maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
      width: 260,
    },
  },
};

export function MultipleSelectCheckmarks(props: MultipleSelectCheckmarksProps) {
  const handleChange = (event: SelectChangeEvent<typeof props.values>) => {
    const {
      target: { value },
    } = event;
    props.setValues(
      typeof value === 'string' ? value.split(';') : value,
    );
  };

  return (
    <div>
      <FormControl sx={{ width: "100%" }}>
        <InputLabel id="multiple-checkbox-label">{ props.label }</InputLabel>
        <Select
          labelId="multiple-checkbox-label"
          id="multiple-checkbox"
          multiple
          value={ props.values }
          onChange={ handleChange }
          input={ <OutlinedInput label={ props.label } /> }
          renderValue={ (selected) => selected.join(', ') }
          MenuProps={ MenuProps }
        >
          {props.selectionList.map((item) => (
            <MenuItem key={ item } value={ item }>
              <Checkbox checked={ props.values.indexOf(item) > -1 } />
              <ListItemText primary={ item } />
            </MenuItem>
          ))}
        </Select>
      </FormControl>
    </div>
  );
}
