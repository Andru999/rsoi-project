import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import FormHelperText from '@mui/material/FormHelperText';
import Select, { SelectChangeEvent } from '@mui/material/Select';


interface SelectRowProps {
  label: string
  selectionList: string[]
	value: string
	setValue: (value: string) => void
  addEmptyElement?: boolean 
  isInvalidRow?: boolean
  selectHandler?: () => void
}

export function SelectRow(props: SelectRowProps) {
  const handleChange = (event: SelectChangeEvent) => {
    props.setValue(event.target.value);

    if (props.selectHandler) {
			props.selectHandler();
		}
  };

  return (
    <div>
      <FormControl 
        fullWidth 
        error={props.isInvalidRow}
      >
        <InputLabel id="simple-select-autowidth-label">{ props.label }</InputLabel>
        <Select
          labelId="simple-select-autowidth-label"
          id="simple-select-autowidth"
          value={ props.value }
          onChange={ handleChange }
          label={ props.label }
        >
          { props.addEmptyElement &&
            <MenuItem value="" key="">
              <em>—</em>
            </MenuItem>
          }  
          { props.selectionList.map(item =>
              <MenuItem value={ item } key={ item }>{ item }</MenuItem>
            )
          }
        </Select>
        {props.isInvalidRow &&
          <FormHelperText>Обязательное поле</FormHelperText>
        }
      </FormControl>
    </div>
  );
}
